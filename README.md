# GameOfLife
A simulation of Conway's Game of Life, using Tkinter.
## How it Works
Conway's game of life is a cellular automaton consisting of a grid of cells which are each alive or dead. Each cycle, the cells either stay aliive, die of come back to life based on a set of rules.
## Rules
* Alive:
    1. If there are less than 2 cells touching the cell, it dies
    2. If there are more than 3 cells touching the cell, it dies
* Dead:
    1. If there are exactly 3 cells touching the cell, it comes back to life