import pygame
from cell import Cell

size = (width, height) = 600, 600
pygame.init()
win = pygame.display.set_mode(size)
clock = pygame.time.Clock()

n = 72
m = 128

running = True

def draw(cell):
    color = (255,255,255)
    if cell.blocked is True:
        color = (0,0,0,0)
    pygame.draw.rect(win, color, ((cell.x)*cell.width, (cell.y)*cell.height, cell.width, cell.height))

while running is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    win.fill(0)

    for i in range(n):
        for j in range(m):
            cell = Cell(i, j, 10, 10);
            if i % 5 == 0 and j % 5 ==0:
                cell.blocked = True
            draw(cell)
    pygame.display.update()
