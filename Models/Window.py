from time import sleep
from tkinter import Canvas, Tk

from Models.Grid import Grid

class Window:
    def __init__(self, master: Tk, resolution: int, grid: Grid) -> None:
        self.grid = grid
        self.resolution = resolution
        self.master = master
        self.run = True
        self.canvas = Canvas(master, width=resolution, height=resolution)
        self.bindings()
        self.canvas.pack()
    
    def bindings(self):
        self.master.bind("<Escape>", lambda _: self.master.destroy())
        self.master.bind("<Button-1>", lambda event: self.clicked(event))
    
    def clicked(self, event):
        size = self.resolution/self.grid.numCells
        self.grid.switchVal(int(event.y/self.grid.numCells), int(event.x/self.grid.numCells))

    
    def displayGraphic(self):
        self.canvas.delete('all')
        for i in range(self.grid.numCells):
            for j in range(self.grid.numCells):
                start = (self.resolution/self.grid.numCells)
                if self.grid.getVal(i, j) == 1:
                    self.canvas.create_rectangle(start*j, start*i, start*j +start, start*i +start, fill="black")
                else:
                    self.canvas.create_rectangle(start*j, start*i, start*j +start, start*i +start, fill="white")
        self.canvas.update()
    
    def chooseStart(self):
        for i in range(self.grid.numCells):
            for j in range(self.grid.numCells):
                start = (self.resolution/self.grid.numCells)
                if self.grid.getVal(i, j) == 1:
                    self.canvas.create_rectangle(start*j, start*i, start*j +start, start*i +start, fill="black")
                else:
                    self.canvas.create_rectangle(start*j, start*i, start*j +start, start*i +start, fill="white")
        self.canvas.update()

    def runSimulation(self):
        while self.run:
            self.displayGraphic()
            self.grid.createNewGen()
            sleep(0.1)