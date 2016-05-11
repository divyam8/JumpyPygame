import pygame,pygame.mixer,random, sys,time

from pygame.locals import *
import splashscreen


pygame.init()
sound=pygame.mixer.Sound('music_background.wav')
explosion=pygame.mixer.Sound('explosion_enemy.wav')
window=pygame.display.set_mode((400,800))
score=0
WINDOWWIDTH=400
WINDOWHEIGHT=800
pygame.display.set_caption("jumpy")
skyblue=(126,192,238)
black=BLACK=(0,0,0)
WHITE=white=(255,255,255)
red=RED=(255,0,0)
blue=(0,0,255)
global x,y

GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR = black

FPSCLOCK=pygame.time.Clock()
gameLoop=True

def get_high_score():
    # Default high score
    high_score = 0
 
    # Try to read the high score from a file
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        message_to_screen3("Last high score is: "+str(high_score),black)
    except IOError:
        # Error reading file, no high score
        message_to_screen1("There is no high score yet.",black)
    except ValueError:
        # There's a file there, but we don't understand the number.
        print("\nI'm confused. Starting with no high score.")
 
    return high_score
 
def save_high_score(new_high_score):
    try:
        # Write the file to disk
        high_score_file = open("high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        # Hm, can't write it.
        print("Unable to save the high score.")

def message_to_screen(msg,color):
      font=pygame.font.SysFont(None, 60)
      screen_text=font.render(msg,True,GREEN)
      window.blit(screen_text,[70,300])
      
def message_to_screen1(msg,color):
      font=pygame.font.SysFont(None, 45)
      screen_text=font.render(msg,True,RED)
      window.blit(screen_text,[30,450])
      
def message_to_screen2(msg,color):
      font=pygame.font.SysFont(None, 45)
      screen_text=font.render(msg,True,GREEN)
      window.blit(screen_text,[30,600])

def message_to_screen3(msg,color):
      font=pygame.font.SysFont(None, 45)
      screen_text=font.render(msg,True,RED)
      window.blit(screen_text,[30,500])

def showGameOverScreen(score):
    gameOverFont = pygame.font.Font('freesansbold.ttf', 100)
    gameSurf = gameOverFont.render('Game', True, red)
    overSurf = gameOverFont.render('Over', True, red)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    high_score=get_high_score()
    if score>high_score:
        # We do! Save to disk
         message_to_screen1("New high score is: "+str(score),black)
         save_high_score(score)
    else:
         message_to_screen2("Better luck next time!!",black)

                    
    message_to_screen("Your score: "+str(score),black)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out any key presses in the event queue

    while True:
        if checkForKeyPress():
            runGame() # clear event queue
            return

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key
def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, black)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def terminate():
    pygame.quit()
    sys.exit()
def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press any key to play.', True, black)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 130)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

def showStartScreen():
    titleFont = pygame.font.Font(None, 100)
    titleSurf1 = titleFont.render('Jumpy', True, WHITE, skyblue)
    titleSurf2 = titleFont.render('Jumpy', True, blue)

    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(white)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get() 
            return
        pygame.display.update()
        FPSCLOCK.tick(10)
        degrees1 += 3 # rotate by 3 degrees each frame
        degrees2 += 7 # rotate by 7 degrees each frame
def keyPressed(inputKey):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[inputKey]:
        return True
    else:
        return False
'''    
def message_to_screen(msg,color):
      font=pygame.font.SysFont(None, 60)
      screen_text=font.render(msg,True,skyblue)
      window.blit(screen_text,[70,300])
'''      
def collide(x,y,j,k,l,m):
      p=x+20
      q=y+20
      if(x>=j and y>=k and x<=j+l and y<=k+m)or(x>=j and q>=k and x<=j+l and q<=k+m)or(p>=j and y>=k and p<=j+l and y<=k+m)or(p>=j and q>=k and p<=j+l and q<=k+m):
                return 1
            
            
      else :
            
            return 0

def tile1():
    
      xr=random.randrange(10,200)
      return xr

def tile2():  
      xr=random.randrange(200,320)
      return xr

def tile3():
      xr=random.randrange(50,200)
      return xr

def tile4():
      xr=random.randrange(50,200)
      return xr


def runGame():
      x=300
      y=650
      y1=699
      y2=300
      x3=100
      x4=80
      y3=500
      y4=100
      w1=150
      w2=250
      score=0
      while True:
            
            sound.play()
            pygame.display.set_caption("JUMPY             "+"YOUR SCORE : " + str(score))


            for event in pygame.event.get(): 
                if event.type == QUIT: 
                     terminate()
                elif event.type == MOUSEBUTTONDOWN:
                     continue
                if keyPressed(K_ESCAPE): 
                     showGameOverScreen(score)  
                elif keyPressed(K_RIGHT) or keyPressed(K_d): 
                     if x<350 :
                         x += 25
                elif keyPressed(K_LEFT) or keyPressed(K_a):
                     if x>30 :
                         x -= 25

            
            pygame.display.update()
            
            window.fill(white)
            
            pygame.draw.rect(window,red,(x,y,20,20))
            
      
            pygame.draw.rect(window,skyblue,[0,y1,w1,25])
            pygame.draw.rect(window,skyblue,[w1+100,y1,400,25])
            
            pygame.draw.rect(window,skyblue,[0,y2,w2,25])
            pygame.draw.rect(window,skyblue,[w2+100,y2,400,25])

            pygame.draw.rect(window,skyblue,[x4,y4,100,25])
            pygame.draw.rect(window,skyblue,[x3,y3,100,25])

            pygame.draw.rect(window,skyblue,[0,0,10,800])
            pygame.draw.rect(window,skyblue,[390,0,10,800])

            drawScore(score)
            FPSCLOCK.tick(35)
            pygame.display.flip()
            
    
            if collide(x,y+10,0,y1,w1,25)or collide(x,y,w1+100,y1,400,25) or collide(x,y,0,y2,w2,25)or collide(x,y,w2+100,y2,400,25) or collide(x,y,x4,y4,100,25) or collide(x,y,x3,y3,100,25):
                               
                     showGameOverScreen(score)
                     pygame.display.update()
                     score=0
            pygame.display.update()        
            y2=y2+5
            y1=y1+5
            y3=y3+5
            y4=y4+5
            if(y1==655):
                score=score+10
            if(y2==655):
                score=score+10
            if(y3==655):
                score=score+5
            if(y4==655):
                score=score+5
                
            if(y2>800):
                  y2=0
                  #score=score+10
                  w2=tile2()
            if(y1>800):
                  y1=0          
                  w1=tile1()
            if(y3>800):
                  x3=tile3()
                  #score=score+10
                  y3=0
            if(y4>800):
                  x4=tile4()
                  y4=0
def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT,y
    x=300
    y=650
    moveX=0
    moveY=0
    y1=699
    y2=300
    x3=200
    x4=300
    y3=650
    y4=250
    w1=150
    w2=250
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF =window
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('jumpy')
    splashscreen.splash_screen() 
    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()
        
if __name__ == '__main__':
    main()
