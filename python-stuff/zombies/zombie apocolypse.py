import time, copy, os #Inport required modules
#Define the landscape for the apocolypse
apocalypse = [
['H','H','H','H','H','C','H','C','H','C','H','H',],
['H','H','H','H','H','C','H','C','H','C','H','H',],
['H','H','H','H','H','C','C','C','C','C','H','H',],
['H','H','H','H','H','H','H','C','H','H','H','H',],
['H','H','H','H','H','H','H','C','H','H','H','H',],
['H','H','H','H','H','H','H','C','H','H','H','H',],
['H','H','H','H','Z','H','H','C','H','H','H','H',],
['H','H','H','H','H','H','H','C','H','H','H','H',],
['H','H','H','H','H','H','H','C','H','H','H','H',],
['H','H','H','H','H','H','H','C','H','H','H','H',],
['H','H','H','H','H','H','H','C','C','C','C','H',],
['H','H','H','H','H','H','H','H','H','H','H','H',]]
def clearScreen():
    os.system('cls')#CLear the screen. Note this will not work in the python terminal
def printGrid(gridToPrint):#Print each line of the landscape
    for i in range(0,len(gridToPrint)):#Iterate through each row
        line = " "
        for j in range(0,len(gridToPrint[0])):#Iterate through each character
            line = line + gridToPrint[i][j] + ' '#Add character to line
        print(line)#Print line
def zombieBite(gridToBite):
    updatedGridToBite = copy.deepcopy(gridToBite)
    for i in range(0,len(gridToBite)):
        for j in range(0,len(gridToBite[0])):#Iterate for the legnth of the row
            if gridToBite[i][j] == 'Z':
                if i > 0 and gridToBite[i - 1][j] != 'C': #Change character to top
                    updatedGridToBite[i - 1][j] = 'Z'
                if i < len(gridToBite) - 1 and gridToBite[i + 1][j] != 'C':#Change character to bottom
                    updatedGridToBite[i + 1][j] = 'Z'
                if j > 0 and gridToBite[i][j - 1] != 'C':#Change character to left
                    updatedGridToBite[i][j - 1] = 'Z'
                if j < len(gridToBite[0]) - 1 and gridToBite[i][j + 1] != 'C':#Change character to right
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
    return updatedGridToBite#Return the new landscape
clearScreen()
printGrid(apocalypse)
gameCycle = 0
print(' Game Cycle: {}'.format(gameCycle))#Print what game cycle we are on
#Game loop
while True:
    time.sleep(0.5)
    gameCycle +=1
    apocalypse = zombieBite(apocalypse)
    clearScreen()
    printGrid(apocalypse)

    print(' Game Cycle: {}'.format(gameCycle))
