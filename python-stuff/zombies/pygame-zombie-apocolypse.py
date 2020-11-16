import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" #Hide welcome message Must be above pygame import
import pygame, sys, copy, time
from pygame.locals import *
# pygame.font.init()
def drawGrid(grid):
    blockSize = 49
    
    global DISPLAYSURF, font1
    for x in range(len(grid[0])):    
        for y in range(len(grid)):
            # print(grid[x][y])
            if grid[y][x] == 'H':
                colour = (102, 255, 51)
                text = font1.render("H", False, (0,0,0))
            elif grid[y][x] == 'C':
                colour = (255, 255, 0)
                text = font1.render("C", False, (0,0,0))
            else:
                colour = (255, 51, 0)
                text = font1.render("Z", False, (0,0,0))
            
            rect = pygame.Rect(x*(blockSize + 1), y*(blockSize + 1), blockSize, blockSize)
            pygame.draw.rect(DISPLAYSURF, colour, rect)
            rectCenter = text.get_rect(center=rect.center)
            DISPLAYSURF.blit(text, rectCenter)

def zombieBite(gridToBite):
    updatedGridToBite = copy.deepcopy(gridToBite)
    for i in range(0,len(gridToBite)):
        for j in range(0,len(gridToBite[0])):
            if gridToBite[i][j] == 'Z':
                if i > 0 and gridToBite[i - 1][j] != 'C':
                    updatedGridToBite[i - 1][j] = 'Z'
                if i < len(gridToBite) - 1 and gridToBite[i + 1][j] != 'C':
                    updatedGridToBite[i + 1][j] = 'Z'
                if j > 0 and gridToBite[i][j - 1] != 'C':
                    updatedGridToBite[i][j - 1] = 'Z'
                if j < len(gridToBite[0]) - 1 and gridToBite[i][j + 1] != 'C':
                    updatedGridToBite[i][j + 1] = 'Z'
                #Diagonals
                if  j > 0 and i > 0 and gridToBite[i-1][j-1] != 'C':#Change character to top left
                    updatedGridToBite[i-1][j-1] = 'Z'
                if  j < len(gridToBite[0]) - 1 and i > 0 and gridToBite[i-1][j+1] != 'C':#Change character to top right
                    updatedGridToBite[i-1][j+1] = 'Z'
                if  j > 0 and i < len(gridToBite) - 1 and gridToBite[i+1][j-1] != 'C':#Change character to bottom left
                    updatedGridToBite[i+1][j-1] = 'Z'
                if  j < len(gridToBite[0]) - 1 and i < len(gridToBite) - 1 and gridToBite[i+1][j+1] != 'C':#Change character to bottom right
                    updatedGridToBite[i+1][j+1] = 'Z'
    return updatedGridToBite
apocalypse = [
['H','H','H','H','H','H','H','C','H','C','H','H',],
['H','H','H','H','H','H','H','C','H','C','H','H',],
['H','H','H','H','H','H','H','C','C','C','H','H',],
['H','H','H','H','H','H','H','C','H','H','H','H',],
['H','H','H','H','H','H','H','C','H','H','H','H',],
['H','H','H','H','H','H','H','C','H','H','H','H',],
['H','H','H','H','H','H','H','C','H','H','H','H',],
['H','H','H','H','H','H','H','C','H','H','H','H',],
['H','H','H','H','H','H','H','C','H','H','H','H',],
['H','H','H','H','H','H','H','C','H','H','H','H',],
['H','H','H','H','H','H','H','C','C','C','C','H',],
['H','H','H','H','H','Z','H','H','H','H','H','H',]]
pygame.init()
FPS = 1
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Zombie apocalypse')
font1 = pygame.font.SysFont('Courier', 30)

while True: # main game loop
    drawGrid(apocalypse)
    apocalypse = zombieBite(apocalypse)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
