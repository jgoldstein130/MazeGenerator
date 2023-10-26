import sys
import pygame
import random
import time

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800

blockSize = 15
horizontal = True

mazeArray = [['.' for x in range(int(SCREEN_HEIGHT / blockSize))] for y in range(int(SCREEN_HEIGHT / blockSize))] #initializing array for pathfinding
pathFindStack = []

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 215, 60)
blue = (0, 0, 255)
orange = (255, 165, 0)

def main():

    pygame.init()
    global screen
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT))
    pygame.display.set_caption("Maze Generation Division Algorithm With Recursive Backtrack Solve")
    screen.fill(white)
    pygame.display.update()

    divide(0, 0, int(SCREEN_HEIGHT / blockSize), int(SCREEN_HEIGHT / blockSize))
    printEnds()
    pathFind()
    printSimplePath()
    #printMazeArray()
    astar()

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
    for x in range(int(SCREEN_HEIGHT / blockSize)):
        for y in range(int(SCREEN_HEIGHT / blockSize)):
            if(x == 0 or y == 0):
                rect = pygame.Rect(x * blockSize, y * blockSize, blockSize, blockSize)
                pygame.draw.rect(screen, black, rect, 0)
                pygame.display.update()
                mazeArray[y][x] = 'W'
            if((x == 0 and y == 0) or (x == int(SCREEN_HEIGHT / blockSize) - 1) and (y == int(SCREEN_HEIGHT / blockSize) - 1)):
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
    endX = int(SCREEN_HEIGHT / blockSize)
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








def astar():
    import math
    size = len(mazeArray)
    costsHolder = [[['' for x in range(3)] for y in range(int(size))] for z in range(int(size))] # array to hold costs for each space
    area = mazeArray

    area[0][0] = 'S' # start space
    area[int(size) - 1][int(size) - 1] = 'E' # end space

    endX = 0 # initialization
    endY = 0

    currentCosts = []

    def printArea():
        for i in area: 
            for j in i:
                print(j,end = " ")
            print()

    def printCosts():
        for i in costsHolder: 
            for j in i:
                print(j,end = " ")
            print()

    def getStartX():
        for i in range(int(size)): # finding start 
            for j in range(int(size)):
                if(area[j][i] == 'S'):
                    return i

    def getStartY():
        for i in range(int(size)): # finding start 
            for j in range(int(size)):
                if(area[j][i] == 'S'):
                    return j

    def getEndX():
        for i in range(int(size)): # finding end 
            for j in range(int(size)):
                if(area[j][i] == 'E'):
                    return i

    def getEndY():
        for i in range(int(size)): # finding end 
            for j in range(int(size)):
                if(area[j][i] == 'E'):
                    return j

    def isWall(x, y):
        if(area[y][x] == 'W'):
            return True
        else:
            return False

    def isClosed(x, y):
        if(area[y][x] == 'C'):
            return True
        else:
            return False

    def hCost(x, y):
        if(not x == getEndX() or not y == getEndY()):
            endX = getEndX()
            endY = getEndY()
            changeX = endX - x
            changeY = endY - y
            distance = int(math.sqrt((changeX * changeX) + (changeY * changeY)) * 10)
            return distance
        else:
            return 0

    def gCost(x, y):

        if((xPos - x == 0 and abs(yPos - y) == 1) or (yPos - y == 0 and abs(xPos - x) == 1)):
            return 10 + costsHolder[yPos][xPos][0]
        else:
            return 14 + costsHolder[yPos][xPos][0]

    def fCost(x, y):
        return(gCost(x, y) + hCost(x, y))

    def getLowestCostPosX():
        # this function is written very poorly but it works
        # I think I should remove the whole current costs thing and instead iterate through
        # the mazeArea and find all of the spots that are not 'C'
        # add the costs of those spots to an array and find the minimum of that
        # Once again I'd just like to say that this code is bad but I wrote it like 3 years ago so whatever.

        # There is also repeated code
        currentCosts = updateCosts()
        lowestCost = currentCosts[0]
        for currCost in currentCosts:
            if currCost < lowestCost:
                for i in range(int(size)):
                    for j in range(int(size)):
                        if(area[i][j] != 'C'):
                            lowestCost = currCost

        for i in range(int(size)):
            for j in range(int(size)):
                if(costsHolder[i][j][2] == lowestCost and area[i][j] != 'C'):
                    return j


    def getLowestCostPosY():
        currentCosts = updateCosts()
        lowestCost = currentCosts[0]
        for currCost in currentCosts:
            if currCost < lowestCost:
                for i in range(int(size)):
                    for j in range(int(size)):
                        if(area[i][j] != 'C'):
                            lowestCost = currCost

        for i in range(int(size)):
            for j in range(int(size)):
                if(costsHolder[i][j][2] == lowestCost and area[i][j] != 'C'):
                    return i


    def calculateCosts(x, y):        

        checkLeft = True
        checkRight = True
        checkUp = True
        checkDown = True

        if(x == 0):
            checkLeft = False
        if(y == 0):
            checkUp = False
        if(x == int(size) - 1):
            checkRight = False
        if(y == int(size) - 1):
            checkDown = False

        if(checkUp):
            if((not isWall(x, y-1)) and (not isClosed(x, y-1))):
                if(not area[y-1][x] == 'E'):
                    area[y-1][x] = 'O'
                costsHolder[y-1][x][0] = gCost(x, y-1)
                costsHolder[y-1][x][1] = hCost(x, y-1)
                costsHolder[y-1][x][2] = fCost(x, y-1)
                currentCosts.append(fCost(x, y-1))
        if(checkDown):
            if((not isWall(x, y+1)) and (not isClosed(x, y+1))):
                if(not area[y+1][x] == 'E'):
                    area[y+1][x] = 'O'
                costsHolder[y+1][x][0] = gCost(x, y+1)
                costsHolder[y+1][x][1] = hCost(x, y+1)
                costsHolder[y+1][x][2] = fCost(x, y+1)
                currentCosts.append(fCost(x, y+1))
        if(checkRight):
            if((not isWall(x+1, y)) and (not isClosed(x+1, y))):
                if(not area[y][x+1] == 'E'):
                    area[y][x+1] = 'O'
                costsHolder[y][x+1][0] = gCost(x+1, y)
                costsHolder[y][x+1][1] = hCost(x+1, y)
                costsHolder[y][x+1][2] = fCost(x+1, y)
                currentCosts.append(fCost(x+1, y))
        if(checkLeft):
            if((not isWall(x-1, y)) and (not isClosed(x-1, y))):
                if(not area[y][x-1] == 'E'):
                    area[y][x-1] = 'O'
                costsHolder[y][x-1][0] = gCost(x-1, y)
                costsHolder[y][x-1][1] = hCost(x-1, y)
                costsHolder[y][x-1][2] = fCost(x-1, y)
                currentCosts.append(fCost(x-1, y))


    def updateCosts():
        currentCosts = []

        for i in range(int(size)):
            for j in range(int(size)):
                if(area[j][i] == 'O' or area[j][i] == 'E'):
                    currentCosts.append(costsHolder[j][i][2])
        return currentCosts


    xPos = getStartX()
    yPos = getStartY()
    endX = getEndX()
    endY = getEndY()
    costsHolder[endY][endX][2] = math.inf
    costsHolder[yPos][xPos][0] = 0

    # the program works but one thing is wrong
    # every time the program picks a new node to check, each node around that node is recaluclated
    # when this happens, the gCosts of those nodes are updated even if the previous gCost was lower
    # the gCost should only be updated if the new gCost is lower

    # i also need to figure out a way to get the final path

    calculateCosts(xPos, yPos)
    updateCosts()
    area[yPos][xPos] = 'C'

    while((xPos != endX) or (yPos != endY)):
        xPos = getLowestCostPosX()
        yPos = getLowestCostPosY()

        color = orange
        rect = pygame.Rect(xPos * blockSize, yPos * blockSize, blockSize, blockSize)
        pygame.draw.rect(screen, color, rect, 0)
        #time.sleep(.1)
        pygame.display.update()

        area[yPos][xPos] = 'C'
        if(yPos == endY and xPos == endX):
            break  
        else: 
            calculateCosts(xPos, yPos)
            updateCosts()

if (__name__ == "__main__"):
    main()