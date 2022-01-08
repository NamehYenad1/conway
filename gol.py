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

newGrid = createArray(10,10)
# print(newGrid)


#computing neighbours
def sumNeighbours(grid): 
    newGenerationGrid = deepcopy(grid)
    for i in range(0, len(grid)): 
            sum =0
            for x in range(0, len(grid[0])):
                sum += grid[i-1][x]
                sum += grid[i-1][x-1]
                sum+= grid[i-1][x+1]
                sum+= grid[i][x-1]
                sum+= grid[i][x+1]
                sum+=grid[i+1][x]
                sum+=grid[i+1][x-1]
                sum+=grid[i+1][x+1]
                #implement rules here
                if((grid[i][x]==1 and sum<2) or(grid[i][x]==1 and sum>3)): 
                    newGenerationGrid[i][x]=0
                elif(grid[i][x]==0 and sum==3):
                    newGenerationGrid[i][x]=1
                else:
                    newGenerationGrid[i][x]=0
                


                






#Testing basic print to console
def printConsole(ticks): 
    for i in range(0, ticks):
        stringToPrint=''
        for i in range(0, len(newGrid)): 
            for x in range(0, len(newGrid[0])):              
                if(newGrid[i][x]==0):
                    stringToPrint = stringToPrint+' '
                    # print(' ',end ='')
                else:
                    stringToPrint = stringToPrint+'*'
                    # print('*',end ='')
            stringToPrint = stringToPrint +'\n'
        print(stringToPrint, end='\r', flush=True)
        time.sleep(0.5)
        print(stringToPrint, end='\r', flush=True)
        


# printConsole(1) 


 
print('\n* *   * * \n ** *** * \n ** *  * *\n** ***** *\n  ****    \n  * ** * *\n   ** * * \n * *** *  \n**  *  ***\n ****   * ')
print("\033[12A")
print('\n* *   * * \n ** *** * \n ** *  * *\n** ***** *\n  ****    \n  * ** * *\n   ** * * \n * *** *  \n**  *  ***\n ****   * ')
time.sleep(0.5)
   

# for x in range(10):
#     print('\n* *   * * \n ** *** * \n ** *  * *\n** ***** *\n  ****    \n  * ** * *\n   ** * * \n * *** *  \n**  *  ***\n ****   * ', end='\r')
#     time.sleep(0.5)
# print()            
    


