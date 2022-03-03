class Grid:

    def __init__(self, array, numCells):
        self.lastArray = [["" for _ in range(numCells)] for _ in range(numCells)]
        self.numCells = numCells
        if array == None:
            self.array = array
        else:
            self.array = [["" for _ in range(numCells)] for _ in range(numCells)]
    
    def __countLiveNeighbours(self, i, j):
        count = 0
        for xOffset in range(-1, 2):
            for yOffset in range(-1, 2):
                x = i+xOffset
                y = j+yOffset
                if x < 0:
                    x = len(self.array)-1
                elif x >= len(self.array):
                    x = 0
                if y < 0:
                    y = len(self.array)-1
                elif y >= len(self.array):
                    y = 0
                count += self.array[x][y]
        return count

    def checkCell(self, i, j):
        count = self.__countLiveNeighbours(self, i, j)
        if self.array[i][j] == 0 and count == 3:
            return 1
        elif self.array[i][j] == 1 and count >=2 and count <=3:
            return 1
        else:
            return 0
    
    def createNewGen(self):
        self.lastArray = self.array
        temp = self.array
        for i in len(self.numCells):
            for j in len(self.numCells):
                temp[i][j] = self.checkCell(i, j)
        self.array = temp
            
