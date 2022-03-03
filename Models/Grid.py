from random import randint

class Grid:

    def __init__(self, numCells, array = None):
        self.lastArray = [["" for _ in range(numCells)] for _ in range(numCells)]
        self.numCells = numCells
        if array == None:
            self.__array = [[randint(0, 1) for _ in range(numCells)] for _ in range(numCells)]
        else:
            self.__array = array
    
    def __countLiveNeighbours(self, i, j):
        count = 0
        for xOffset in range(-1, 2):
            for yOffset in range(-1, 2):
                if xOffset  != 0 or yOffset != 0:
                    x = i+xOffset
                    y = j+yOffset
                    if x < 0:
                        x = self.numCells-1
                    elif x >= self.numCells:
                        x = 0
                    if y < 0:
                        y = self.numCells-1
                    elif y >= self.numCells:
                        y = 0
                    count += self.__array[x][y]
        return count

    def checkCell(self, i, j):
        count = self.__countLiveNeighbours(i, j)
        if count == 3:
            return 1
        elif count == 2:
            return self.__array[i][j]
        else:
            return 0

    
    def createNewGen(self):
        changes = []
        for i in range(self.numCells):
            for j in range(self.numCells):
                newCell = self.checkCell(i, j)
                if newCell != self.__array[i][j]:
                    changes.append((newCell, i, j))
        for change in changes:
            self.__array[change[1]][change[2]] = change[0]
    
    def getVal(self, i, j):
        return self.__array[i][j]
    
    def getArray(self):
        return self.__array
    
    def switchVal(self, i, j):
        self.__array[i][j] = 1- self.__array[i][j]
            
