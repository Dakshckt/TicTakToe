import pygame 
import numpy as np
import tkinter
from tkinter import messagebox


WIDTH , HEIGHT = 600 , 700
WIN = pygame.display.set_mode((WIDTH , HEIGHT))
size = 200
arr = [ 
            (0,0,size,size),
            (200,0,size,size),
            (400,0,size,size),
            (0,200,size,size),
            (200,200,size,size),
            (400,200,size,size),
            (0,400,size,size),
            (200,400,size,size),
            (400,400,size,size)
    ]
actuallArray = [None , None , None , None , None , None , None , None , None]
XorY = True
moveCount = 0
pygame.font.init()
font1 = pygame.font.SysFont('comicsans' , 25 , True)



def drawWindow():
    global font1
    WIN.fill((255,255,255))

    pygame.draw.rect(WIN , (255,255,255) , (0 , HEIGHT-100 , WIDTH  , abs(100 - HEIGHT)))

    for val in arr:
        pygame.draw.rect(WIN , (0,0,0) , val , 1)

    text1 = font1.render('X Turn' , 1 , (0,0,0))
    WIN.blit(text1 , (250 , 630))
    
    pygame.display.update()




def drawX(x , y):
    global font1

    pygame.draw.rect(WIN , (255,255,255) , (250 , 630 , 100 , 50))

    xLetter = pygame.image.load('./AllPhotos/Xletter.png')
    xLetter = pygame.transform.scale(xLetter , (200 , 200))
    WIN.blit(xLetter , (x , y))

    text1 = font1.render('O Turn' , 1 , (0,0,0))
    WIN.blit(text1 , (250 , 630))

    pygame.display.update()




    
def drawO(x , y):
    global font1

    pygame.draw.rect(WIN , (255,255,255) , (250 , 630 , 100 , 50))

    oLetter = pygame.image.load('./AllPhotos/Oletter.png')
    oLetter = pygame.transform.scale(oLetter , (200 , 200))
    WIN.blit(oLetter , (x , y))
    
    text1 = font1.render('X Turn' , 1 , (0,0,0))
    WIN.blit(text1 , (250 , 630))

    pygame.display.update()


def gameOver(player):
    global actuallArray , XorY , moveCount
    if player != None:
        messagebox.showinfo("Game Over",f"Player Plaing with {player} is winner")
    else:
        messagebox.showinfo("Game Over","Both the player Had A Draw")
    actuallArray = [None , None , None , None , None , None , None , None , None]
    XorY = True
    moveCount = 0
    player = None
    drawWindow()


drawWindow()

def main():
    pygame.init()
    
    global arr , XorY , moveCount
    run = True
    player = None

    xLetter = pygame.image.load('./AllPhotos/Xletter.png')
    oLetter = pygame.image.load('./AllPhotos/Oletter.png')
    xLetter = pygame.transform.scale(xLetter , (200 , 200))
    oLetter = pygame.transform.scale(oLetter , (200 , 200))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

                for index , cordi in enumerate(arr):
                    if x > cordi[0] and y > cordi[1] and x < cordi[0] + 200 and y < cordi[1] + 200:

                        if XorY == True and actuallArray[index] != 'X' and actuallArray[index] != 'O':
                            actuallArray[index] = 'X'
                            XorY = False
                            moveCount = moveCount + 1
                            drawX(cordi[0] , cordi[1])
                            # print(actuallArray)

                        elif XorY == False and actuallArray[index] != 'X' and actuallArray[index] != 'O':
                            actuallArray[index] = 'O'
                            XorY = True
                            moveCount = moveCount + 1
                            drawO(cordi[0] , cordi[1])
                            # print(actuallArray)


                        
                        for i in range(0, 9 ,3):
                            if actuallArray[i] == actuallArray[i+1] == actuallArray[i+2] == 'X':
                                player = 'X'
                                gameOver(player)
                            elif actuallArray[i] == actuallArray[i+1] == actuallArray[i+2] == 'O':
                                player = 'O'
                                gameOver(player)

                        
                        for i in range(0 , 3):
                            if actuallArray[i] == actuallArray[i+3] == actuallArray[i+6] == 'X':
                                player = 'X'
                                gameOver(player)

                            elif actuallArray[i] == actuallArray[i+3] == actuallArray[i+6] == 'O':
                                player = 'O'
                                gameOver(player)

                        if actuallArray[0] == actuallArray[4] == actuallArray[8] == 'X':
                            player = 'X'
                            gameOver(player)
                        if actuallArray[0] == actuallArray[4] == actuallArray[8] == 'O':
                            player = 'O'
                            gameOver(player)
                        if actuallArray[2] == actuallArray[4] == actuallArray[6] == 'X':
                            player = 'X'
                            gameOver(player)
                        if actuallArray[2] == actuallArray[4] == actuallArray[6] == 'O':
                            player = 'O'
                            gameOver(player)


                    if moveCount >= 9:
                        player = None
                        gameOver(player)

                
            if event.type == pygame.QUIT:
                run = False



    pygame.quit()

if __name__ == '__main__':
    main()