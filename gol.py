import random
from copy import copy, deepcopy
#create 2d array first to simulate a grid
def createArray(columns, rows):
    grid = []
    for i in range(0, columns): 
        col=[]
        for x in range(0, rows): 
            col.append(random.randint(0,1))
        grid.append(col)
    return grid

newGrid = createArray(10,10)
print(newGrid)


#computing neighbours
def sumNeighbours(grid): 
    newGenerationGrid = deepcopy(grid)
    for i in range(0, len(grid)): 
            sum =0
            for x in range(0, len(grid[0])):


                






#Testing basic print to console
def printConsole(ticks): 
    for i in range(0, ticks):
        for i in range(0, len(newGrid)): 
            for x in range(0, len(newGrid[0])):
                if(newGrid[i][x]==0):
                    print(' ',end ='')
                else:
                    print('*',end ='')
                
printConsole(1) 

                
    


