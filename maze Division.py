import sys
import pygame
import random
import time

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

blockSize = 10
horizontal = True

mazeArray = [['.' for x in range(int(SCREEN_WIDTH / blockSize))] for y in range(int(SCREEN_HEIGHT / blockSize))] #initializing array for pathfinding
pathFindStack = []

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 215, 60)
blue = (0, 0, 255)

def main():

    pygame.init()
    global screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Maze Generation Division Algorithm With Recursive Backtrack Solve")
    screen.fill(white)
    pygame.display.update()

    divide(0, 0, int(SCREEN_WIDTH / blockSize), int(SCREEN_HEIGHT / blockSize))
    printEnds()
    pathFind()
    printSimplePath()

    while True:        
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
        pygame.display.update()



def divide(startX, startY, endX, endY):
    
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()
    
    ranDirection = random.randint(1, 2)
    if(ranDirection == 1):
        horizontal = True
    else:
        horizontal = False

    
    if(horizontal):

        mid = random.randrange(startY, endY, 2)

        for x in range(startX, endX):
            rect = pygame.Rect(x * blockSize, mid * blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, black, rect, 0)
            pygame.display.update()
            #time.sleep(.01)
            mazeArray[mid][x] = 'W'
        
        hole = random.randrange(startX + 1, endX - 1, 2)
        rect = pygame.Rect(hole * blockSize, mid * blockSize, blockSize, blockSize)
        pygame.draw.rect(screen, white, rect, 0)
        mazeArray[mid][hole] = '.'
        
        #print(mid)
        if(mid - startY > 2):
            divide(startX, startY, endX, mid)
        if(endY - mid > 2):
            divide(startX, mid, endX, endY)
    

    else:

        mid = random.randrange(startX, endX, 2)

        for y in range(startY, endY):
            rect = pygame.Rect(mid * blockSize, y * blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, black, rect, 0)
            pygame.display.update()
            #time.sleep(.01)
            mazeArray[y][mid] = 'W'
        
        hole = random.randrange(startY + 1, endY - 1, 2)
        rect = pygame.Rect(mid * blockSize, hole * blockSize, blockSize, blockSize)
        pygame.draw.rect(screen, white, rect, 0)
        mazeArray[hole][mid] = '.'
        
        #print(mid)
        if(mid - startX > 2):
            divide(startX, startY, mid, endY)
        if(endX - mid > 2):
            divide(mid, startY, endX, endY)



def printEnds():
    for x in range(int(SCREEN_WIDTH / blockSize)):
        for y in range(int(SCREEN_HEIGHT / blockSize)):
            if(x == 0 or y == 0):
                rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
                pygame.draw.rect(screen, black, rect, 0)
                pygame.display.update()
                mazeArray[y][x] = 'W'
            if((x == 0 and y == 0) or (x == int(SCREEN_WIDTH / blockSize) - 1) and (y == int(SCREEN_HEIGHT / blockSize) - 1)):
                rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
                pygame.draw.rect(screen, red, rect, 0)
                pygame.display.update()
                mazeArray[y][x] = '.'
            if(x == 0 and y == 1):
                rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
                pygame.draw.rect(screen, white, rect, 0)
                pygame.display.update()
                mazeArray[y][x] = '.'
            if(x == 1 and y == 0):
                rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
                pygame.draw.rect(screen, white, rect, 0)
                pygame.display.update()
                mazeArray[y][x] = '.'



def printMazeArray():
    for i in mazeArray: # printing the maze array for pathfinding testing
        for j in i:
            print(j,end = "")
        print()



def pathFind():

    x = 0
    y = 0
    mazeArray[y][x] = 'V'
    endX = int(SCREEN_WIDTH / blockSize)
    endY = int(SCREEN_HEIGHT / blockSize)
    color = green

    while(True):

        canMoveUp = False
        canMoveDown = False
        canMoveLeft = False
        canMoveRight = False

        moveUp = False
        moveDown = False
        moveLeft = False
        moveRight = False

        if(x > 0):
            canMoveLeft = True
        if(y > 0):
            canMoveUp = True
        if(x < endX - 1):
            canMoveRight = True
        if(y < endY - 1):
            canMoveDown = True

        if(canMoveUp and mazeArray[y - 1][x] != 'W' and mazeArray[y - 1][x] != 'V'):
            moveUp = True
            pathFindStack.append(x)
            pathFindStack.append(y)
            y -= 1
            mazeArray[y][x] = 'V'
            rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, color, rect, 0)
            pygame.display.update()
            color = green
        elif(canMoveRight and mazeArray[y][x + 1] != 'W' and mazeArray[y][x + 1] != 'V'):
            moveRight = True
            pathFindStack.append(x)
            pathFindStack.append(y)
            x += 1
            mazeArray[y][x] = 'V'
            rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, color, rect, 0)
            pygame.display.update()
            color = green
        elif(canMoveDown and mazeArray[y + 1][x] != 'W' and mazeArray[y + 1][x] != 'V'):
            moveDown = True
            pathFindStack.append(x)
            pathFindStack.append(y)
            y += 1
            mazeArray[y][x] = 'V'
            rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, color, rect, 0)
            pygame.display.update()
            color = green
        elif(canMoveLeft and mazeArray[y][x - 1] != 'W' and mazeArray[y][x - 1] != 'V'):
            moveLeft = True
            pathFindStack.append(x)
            pathFindStack.append(y)
            x -= 1
            mazeArray[y][x] = 'V'
            rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, color, rect, 0)
            pygame.display.update()
            color = green

        if(x == endX - 1 and y == endY - 1):
            return

        if((not moveUp) and (not moveDown) and (not moveRight) and (not moveLeft)):
            y = pathFindStack.pop()
            x = pathFindStack.pop()
            color = red
            rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
            pygame.draw.rect(screen, color, rect, 0)



def printSimplePath():
    for i in range(int(len(pathFindStack) / 2)):
        y = pathFindStack.pop()
        x = pathFindStack.pop()
        color = blue
        rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
        pygame.draw.rect(screen, color, rect, 0)
        #time.sleep(.1)
        pygame.display.update()



if (__name__ == "__main__"):
    main()