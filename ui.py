import pygame
import math
from algorithm import *

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
            print(cell_pos)
            cells[math.floor(cell_pos[0])][math.floor(cell_pos[1])] = 1
            if math.floor(cell_pos[0]) == 49 and math.floor(cell_pos[1]) == 99:
                running = 0

    for i in range(n):
        for j in range(m):
            cell = cells[i][j]
            draw(i, j)
    pygame.display.update()
    
Lee()
_cout()
