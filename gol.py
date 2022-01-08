import random
import time
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

#update grid
def upDateGrid(): 
    global Grid
    newGenerationGrid = deepcopy(Grid)
    for i in range(0, len(Grid)): 
            for x in range(0, len(Grid[0])):
                sum =0
                for a in range(-1, 2): 
                    sum += Grid[(i+a+len(Grid))% len(Grid)][(x+a+len(Grid))%len(Grid[0])] 
        
                #implement rules here
                if((Grid[i][x]==1 and sum<2) or(Grid[i][x]==1 and sum>3)): 
                    newGenerationGrid[i][x]=0
                elif((Grid[i][x]==0 and sum==3) or(Grid[i][x]==1 and (sum==2 or sum == 3))):
                    newGenerationGrid[i][x]=1
                else:
                    newGenerationGrid[i][x]=0


    Grid = newGenerationGrid


#SumOfNeighbours 

def calculateSum():
    

    for i in range(0, len(Grid)): 
            for x in range(0, len(Grid[0])):
                
                sum =0
                sum += Grid[(i-1+len(Grid)) % len(Grid)][(x+len(Grid)) % len(Grid[0])]
                sum += Grid[(i-1+len(Grid))% len(Grid)][(x-1+len(Grid))% len(Grid[0])]
                sum+= Grid[(i-1+len(Grid)) % len(Grid)][(x+1+len(Grid))% len(Grid[0])]
                sum+= Grid[i+len(Grid) % len(Grid)][(x-1+len(Grid))% len(Grid[0])]
                sum+= Grid[i+len(Grid) % len(Grid)][(x+1+len(Grid)) % len(Grid[0])]
                sum+=Grid[(i+1+len(Grid)) % len(Grid)][(x+len(Grid))% len(Grid[0])]
                sum+=Grid[(i+1+len(Grid)) % len(Grid)][(x-1+len(Grid))% len(Grid[0])]
                sum+=Grid[(i+1+len(Grid)) % len(Grid)][(x+1+len(Grid))% len(Grid[0])]
        






    
                
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
    print("\033[13A")

                
# def main(): 
#     ticks = int(input("Enter lifespan: "))
#     for i in range(0, ticks): 
#         print(i)
#         printGrid()
#         moveCursorToTop()
#         upDateGrid()
#         time.sleep(0.5)

# main()



for i in range(-1,2):
    print(i)
 




