import time
from tkinter import Tk
from Models.Grid import Grid
from Models.Window import Window
resolution = 500
master = Tk()


def createEmptyBoard(n):
  grid5 = [[0 for _ in range(n)] for _ in range(n)]
  return Grid(n, grid5)

def createCustomBoard(n):
  grid6 = [["" for _ in range(n)] for _ in range(n)]
  repeat = True
  while repeat == True:
    if input('add a live cell?') != 'y':
      repeat = False
      break
    else:
      i = int(input('Which column?'))
      j = int(input('Which row?'))
      grid6[i][j] = 1
  return Grid(n, grid6)

def runSimulation(window: Window):

  while True:
    window.displayGraphic()
    window.grid.createNewGen()
    input()

def setup():
  master.title('Game of Life')
  window = Window(master, resolution, Grid(25))
  # window.chooseStart()
  window.runSimulation()

if __name__ == "__main__":
  setup()