import random
# import time
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

Grid = createArray(10,10)

#counting neightbours


#update grid
def upDateGrid(): 
    global Grid
    newGenerationGrid = deepcopy(Grid)
 
 

    for i in range(0, len(Grid)): 
            sum =0
            for x in range(0, len(Grid[0])):
                
                # When location is at edges, find way to wrap around to other side error is when dealing with the out edges of the grid, looping over array will go out of bounds, finding a way to wrap around the edges of the grid by drawing and visualizing on physical piece of paper

                sum += Grid[(i-1+len(Grid)) % len(Grid)][(x+len(Grid)) % len(Grid[0])]
                sum += Grid[(i-1+len(Grid))% len(Grid)][(x-1+len(Grid))% len(Grid[0])]
                sum+= Grid[(i-1+len(Grid)) % len(Grid)][(x+1+len(Grid))% len(Grid[0])]
                sum+= Grid[i+len(Grid) % len(Grid)][(x-1+len(Grid))% len(Grid[0])]
                sum+= Grid[i+len(Grid) % len(Grid)][(x+1+len(Grid)) % len(Grid[0])]
                sum+=Grid[(i+1+len(Grid)) % len(Grid)][(x+len(Grid))% len(Grid[0])]
                sum+=Grid[(i+1+len(Grid)) % len(Grid)][(x-1+len(Grid))% len(Grid[0])]
                sum+=Grid[(i+1+len(Grid)) % len(Grid)][(x+1+len(Grid))% len(Grid[0])]
        
                #implement rules here
                if((Grid[i][x]==1 and sum<2) or(Grid[i][x]==1 and sum>3)): 
                    newGenerationGrid[i][x]=0
                elif(Grid[i][x]==0 and sum==3):
                    newGenerationGrid[i][x]=1
                else:
                    newGenerationGrid[i][x]=0
    Grid = newGenerationGrid
    
                
def printGrid(): 
    stringToPrint=''
    global Grid
    for i in range(0, len(Grid)): 
            for x in range(0, len(Grid[0])):              
                if(Grid[i][x]==0):
                    stringToPrint = stringToPrint+' '
                else:
                    stringToPrint = stringToPrint+'*'
            stringToPrint = stringToPrint +'\n'
    print(stringToPrint)

def moveCursorToTop():
    print("\033[12A")

                

# #Testing basic print to console
# def printGrid(ticks): 
#     for i in range(0, ticks):
#         stringToPrint=''
#         for i in range(0, len(newGrid)): 
#             for x in range(0, len(newGrid[0])):              
#                 if(newGrid[i][x]==0):
#                     stringToPrint = stringToPrint+' '
#                     # print(' ',end ='')
#                 else:
#                     stringToPrint = stringToPrint+'*'
#                     # print('*',end ='')
#             stringToPrint = stringToPrint +'\n'
#         print(stringToPrint, end='\r', flush=True)
#         time.sleep(0.5)
#         print(stringToPrint, end='\r', flush=True)


def main(): 
    ticks = int(input("Enter lifespan: "))
    for i in range(0, ticks): 
        printGrid()
        moveCursorToTop()
        upDateGrid()
        

main()




 




