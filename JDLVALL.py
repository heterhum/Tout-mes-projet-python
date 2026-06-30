import numpy as np
import pygame
import random as rd
TAILLEX = 50
TAILLEY = 50
N = 20
time=500 #ms
MOVE = [(1, 1), (0, 1), (-1, 1),(1, -1), (0, -1), (-1, -1),(1, 0), (-1, 0)]
grille_num = [[0 for j in range(TAILLEX)] for i in range(TAILLEY)]
screen = pygame.display.set_mode((N * TAILLEX, N * TAILLEY))
fist_grille = True
pause=True
running = True

def NeighborNumber(grille,x,y):
    s = 0
    for i in MOVE:
        x1, y1 = i
        if 0 <= x + x1 < TAILLEX and 0 <= y + y1 < TAILLEY:
            if grille[y + y1][x + x1] == 1:
                s += 1
    return s

def NeighborAt(grille,x,y,x1,y1):
    if 0 <= x + x1 < TAILLEX and 0 <= y + y1 < TAILLEY:
        if grille[y + y1][x + x1] == 1:
            return True
        else:
            return False
    else: 
        return False

def check(grille, x, y):
    s = NeighborNumber(grille,x,y)
    if s == 3:
        return 1
    elif NeighborAt(grille,x,y,2,-3):
        return 0
    elif s == 2:
        return grille[y][x]
    elif s==7:
        return 1
    else:
        return 0

def Randomise(grille,pourcentage):
    for y in range(TAILLEY):
        for x in range(TAILLEX):
            r=rd.random()
            if r<=pourcentage:
                grille[y][x] = 1
            else:
                grille[y][x] = 0
    return grille

def main(g):
    grilles=[i.copy() for i in g]
    for y in range(TAILLEY):
        for x in range(TAILLEX):
            grille_num[y][x] = check(grilles, x, y)

def dess(grille):
    for y in range(TAILLEY):
        for x in range(TAILLEX):
            if grille[y][x] == 1:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x * N, y * N, N - 1, N - 1))
            else:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x * N, y * N, N - 1, N - 1))

while running:
    dess(grille_num)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if event.button==1:
                grille_num[pos[1] // N][pos[0] // N] = 1
            if event.button==3:
                grille_num[pos[1] // N][pos[0] // N] = 0
        if event.type == pygame.KEYDOWN and event.key==pygame.K_p: pause=not pause
        if event.type == pygame.KEYDOWN and event.key==pygame.K_r and pause: grille_num=Randomise(grille_num,0.1)

    if not pause:
        main(grille_num)
        pygame.time.wait(time)

    pygame.display.update()
quit()