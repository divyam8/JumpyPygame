import pygame
from pygame.locals import *
import sys
import time
import pyganim

window=pygame.display.set_mode((400,800))
pygame.display.set_caption("JUMPY")

loadnames=pygame.image.load('loading/loadingnames.png').convert_alpha()
BGCOLOR = (250, 250, 245)
window.fill(BGCOLOR)
pygame.display.update() 
def splash_screen():
       
    loadanim = pyganim.PygAnimation([('loading/a_0000.png', 0.025),
                                     ('loading/a_0001.png', 0.025),
                                     ('loading/a_0002.png', 0.025),
                                     ('loading/a_0003.png', 0.025),
                                     ('loading/a_0004.png', 0.025),
                                     ('loading/a_0005.png', 0.025),
                                     ('loading/a_0006.png', 0.025),
                                     ('loading/a_0007.png', 0.025),
                                     ('loading/a_0008.png', 0.025),
                                     ('loading/a_0009.png', 0.025),
                                     ('loading/a_0010.png', 0.025),
                                     ('loading/a_0011.png', 0.025),
                                     ('loading/a_0012.png', 0.025),
                                     ('loading/a_0013.png', 0.025),
                                     ('loading/a_0014.png', 0.025),
                                     ('loading/a_0015.png', 0.025),
                                     ('loading/a_0016.png', 0.025),
                                     ('loading/a_0017.png', 0.025),
                                     ('loading/a_0018.png', 0.025),
                                     ('loading/a_0019.png', 0.025),
                                     ('loading/a_0020.png', 0.025),
                                     ('loading/a_0021.png', 0.025),
                                     ('loading/a_0022.png', 0.025),
                                     ('loading/a_0023.png', 0.025),
                                     ('loading/a_0024.png', 0.025),
                                     ('loading/a_0025.png', 0.025),
                                     ('loading/a_0026.png', 0.025),
                                     ('loading/a_0027.png', 0.025),
                                     ('loading/a_0028.png', 0.025),
                                     ('loading/a_0029.png', 0.025),
                                     ('loading/a_0030.png', 0.025),
                                     ('loading/a_0031.png', 0.025),
                                     ('loading/a_0032.png', 0.025),
                                     ('loading/a_0033.png', 0.025),
                                     ('loading/a_0034.png', 0.025),
                                     ('loading/a_0035.png', 0.025),
                                     ('loading/a_0036.png', 0.025),
                                     ('loading/a_0037.png', 0.025),
                                     ('loading/a_0039.png', 0.025),
                                     ('loading/a_0040.png', 0.025),
                                     ('loading/a_0041.png', 0.025),
                                     ('loading/a_0042.png', 0.025),
                                     ('loading/a_0043.png', 0.025),
                                     ('loading/a_0044.png', 0.025),
                                     ('loading/a_0045.png', 0.025),
                                     ('loading/a_0046.png', 0.025),
                                     ('loading/a_0047.png', 0.025),
                                     ('loading/a_0048.png', 0.025),
                                     ('loading/a_0049.png', 0.025),
                                     ('loading/a_0050.png', 0.025),
                                     ('loading/a_0051.png', 0.025),
                                     ('loading/a_0052.png', 0.025),
                                     ('loading/a_0053.png', 0.025),
                                     ('loading/a_0054.png', 0.025),
                                     ('loading/a_0055.png', 0.025),
                                     ('loading/a_0056.png', 0.025),
                                     ('loading/a_0057.png', 0.025),
                                     ('loading/a_0058.png', 0.025),
                                     ('loading/a_0059.png', 0.025),
                                     ('loading/a_0060.png', 0.025),
                                     ('loading/a_0061.png', 0.025),
                                     ('loading/a_0062.png', 0.025),
                                     ('loading/a_0063.png', 0.025),
                                     ('loading/a_0064.png', 0.025),
                                     ('loading/a_0065.png', 0.025),
                                     ('loading/a_0066.png', 0.025),
                                     ('loading/a_0067.png', 0.025),
                                     ('loading/a_0068.png', 0.025),
                                     ('loading/a_0069.png', 0.025),
                                     ('loading/a_0070.png', 0.025),
                                     ('loading/a_0071.png', 0.025),
                                     ('loading/a_0072.png', 0.025),
                                     ('loading/a_0073.png', 0.025),
                                     ('loading/a_0074.png', 0.025),
                                     ('loading/a_0075.png', 0.025),
                                     ('loading/a_0076.png', 0.025),
                                     ('loading/a_0077.png', 0.025),
                                     ('loading/a_0078.png', 0.025),
                                     ('loading/a_0079.png', 0.025),
                                     ('loading/a_0080.png', 0.025),
                                     ('loading/a_0081.png', 0.025),
                                     ('loading/a_0082.png', 0.025),
                                     ('loading/a_0083.png', 0.025),
                                     ('loading/a_0084.png', 0.025),
                                     ('loading/a_0085.png', 0.025),
                                     ('loading/a_0086.png', 0.025),
                                     ('loading/a_0087.png', 0.025),
                                     ('loading/a_0088.png', 0.025),
                                     ('loading/a_0089.png', 0.025),
                                     ('loading/a_0090.png', 0.025),
                                     ('loading/a_0091.png', 0.025),
                                     ('loading/a_0092.png', 0.025),
                                     ('loading/a_0093.png', 0.025),
                                     ('loading/a_0094.png', 0.025),
                                     ('loading/a_0005.png', 0.025)])

   
    
   
    loadanim.play()    # start playing the fire animations
    

    mainClock = pygame.time.Clock()
    BGCOLOR = (250, 250, 245)
    window.fill(BGCOLOR)
    i=0
    while i<100:
   
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
           
   
        
        loadanim.blit(window, (0,0))
        window.blit(loadnames,[0,300])

        pygame.display.update()
        mainClock.tick(30) #FPS setting.
        i=i+1
        

    
    loadanim.stop()
    window.fill(BGCOLOR)
    pygame.display.update()

#splash_screen()
