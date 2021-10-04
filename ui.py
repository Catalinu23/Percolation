import pygame
import math


n = int(input())
m = int(input())

def_w = 480
def_h = 360

screen_w = def_w
screen_h = math.floor(def_w * n/m) + 1

cell_w = math.floor(def_w/m)
cell_h = math.floor(def_h/n)

cells = [[0 for x in range(1000)] for y in range(1000)]

for i in range(n):
    for j in range(m):
        cells[i][j] = False

size = (width, height) = screen_w, screen_h
pygame.init()
win = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True

def draw(x, y):
    color = (255,255,255)
    if cells[x][y] == True:
        color = (0,0,0,0)
        # print(cell.x)
    pygame.draw.rect(win, color, ((x)*cell_w, (y)*cell_h, cell_w, cell_h))
    pygame.draw.rect(win, (0,0,0,0), ((x)*cell_w, (y)*cell_h, cell_w, cell_h), 1)

def get_cell(x, y):
    return (x/cell_w, y/cell_h)

while running is True:

    win.fill(0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            cell_pos = get_cell(pos[0], pos[1])
            print(cell_pos)
            cells[math.floor(cell_pos[0])][math.floor(cell_pos[1])] = True

    for i in range(n):
        for j in range(m):
            cell = cells[j][i]
            # if i % 5 == 0 and j % 5 ==0:
            #     cell.blocked = True
            draw(j, i)
    pygame.display.update()
