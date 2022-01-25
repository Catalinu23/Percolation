import pygame
import math
#from algorithm import *

n = 100
m = 50

def_w = 500
def_h = 1000

screen_w = 1000
screen_h = 500

cell_w = math.floor(def_w/m)
cell_h = math.floor(def_h/n)

cells = [[0 for x in range(1000)] for y in range(1000)]

for i in range(n):
    for j in range(m):
        cells[i][j] = 0

size = (width, height) = screen_w, screen_h
pygame.init()
win = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = 1

def draw(x, y):
    color = (255,255,255)
    if cells[x][y] == 1:
        color = (0,0,0,0)
    pygame.draw.rect(win, color, ((x)*cell_w, (y)*cell_h, cell_w, cell_h))
    pygame.draw.rect(win, (0,0,0,0), ((x)*cell_w, (y)*cell_h, cell_w, cell_h), 1)

def get_cell(x, y):
    return (x/cell_w, y/cell_h)

while running == 1:

    win.fill(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            cell_pos = get_cell(pos[0], pos[1])
            cells[math.floor(cell_pos[0])][math.floor(cell_pos[1])] = 1

    for i in range(n):
        for j in range(m):
            cell = cells[i][j]
            draw(i, j)
    pygame.display.update()

queue = []
track = [[0 for i in range(1000)] for j in range(1000)]
di = [0 , 0 , 1 , -1]
dj = [1 , -1 , 0 , 0]

def inMatrix(i : int , j : int):
    if i >= 0 and i < 50 and j >= 0 and j < 100:
        return 1
    return 0

def Lee():
    for col in range(101):
        if cells[0][col] == 0:
            queue.append((0 , col))
            track[0][col] = 1
    while len(queue) > 0:
        i = queue[0][0]
        j = queue[0][1]
        queue.pop(0)
        for k in range(4):
            newI = i + di[k]
            newJ = j + dj[k]
            if inMatrix(newI , newJ) and cells[newI][newJ] == 0 and track[newI][newJ] == 0:
                queue.append((newI , newJ))
                track[newI][newJ] = track[i][j] + 1

def _cout():
    maxim = 0
    for col in range(100):
        if track[49][col] > maxim:
            maxim = track[49][col]
    print(maxim)

Lee()
_cout()
