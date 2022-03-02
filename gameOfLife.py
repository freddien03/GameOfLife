import random
import time
from tkinter import Tk, Canvas
global resolution
resolution = 500

def create2DArray(n):
  grid = []
  for i in range(n):
    grid.append([])
    for _ in range(n):
      grid[i].append('')
  return grid

def countLiveNeighbours(grid1, i, j):
  x = 3
  y = 3
  z = 0
  zz = 0
  if i == len(grid1)-1:
    x = 2
  if j == len(grid1)-1:
    y = 2
  if i == 0:
    x = 2
    z = 1
  if j == 0:
    y = 2
    zz = 1
  count = 0
  for ii in range(x):
    for jj in range(y):
      if ii != 1-z or jj != 1-zz:
        count += grid1[i-1+ii+z][j-1+jj+zz]
  return count

def checkToDeath(grid3, i, j):
  count = countLiveNeighbours(grid3, i, j)
  if count<2 or count>3:
    return 0
  else:
    return 1

def checkToLife(grid2, i, j):
  count = countLiveNeighbours(grid2, i, j)
  if count==3:
    return 1
  else:
    return 0

def createNewGen(old):
  change = []
  for i in range(len(old)):
    for j in range(len(old[i])):
      if old[i][j] == 0:
        if checkToLife(old, i, j) == 1:
          change.append([i,j,1])
      else:
        if checkToDeath(old, i, j) == 0:
          change.append([i,j,0])
  for item in change:
    old[item[0]][item[1]] = item[2]
  return old

def createRandBoard(n):
  grid4 = create2DArray(n)
  for i in range(n):
    for j in range(n):
      grid4[i][j] = random.randint(0, 1)
  return grid4

def createEmptyBoard(n):
  grid5 = create2DArray(n)
  for i in range(n):
    for j in range(n):
      grid5[i][j] = 0
  return grid5

def createCustomBoard(n):
  grid6 = createEmptyBoard(n)
  repeat = True
  while repeat == True:
    if input('add a live cell?') != 'y':
      repeat = False
      break
    else:
      i = int(input('Which column?'))
      j = int(input('Which row?'))
      grid6[i][j] = 1
  return grid6

def runSimulation(grid8):

  while True:
    displayGraphic(grid8, len(grid8))
    grid8 = createNewGen(grid8)

def displayBoard(grid7):
  for i in range(len(grid7)):
    for j in range(len(grid7[i])):
      if grid7[i][j] == 0:
        print(' ', end = ' ')
      elif grid7[i][j] == 1:
        print('O', end = ' ')
      else:
        print(grid7[i][j], end = ' ')
    print('')

def displayGraphic(grid, n):
  w.delete('all')
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      start = (resolution/n)
      if grid[i][j] == 1:
        w.create_rectangle(start*i, start*j, start*i +start, start*j +start, fill="black")
      else:
        w.create_rectangle(start*i, start*j, start*i +start, start*j +start, fill="white")
  w.update()

def setup():
  global w
  master = Tk()
  master.title('Game of Life')
  w = Canvas(master, width=resolution, height=resolution)
  w.pack()
  mainGrid = createRandBoard(25)
##  mainGrid = createCustomBoard(25)
  runSimulation(mainGrid)

setup()
