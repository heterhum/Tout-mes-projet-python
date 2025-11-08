import pygame
import numpy as np
import copy
import time
WIDTH, HEIGHT = 1000, 600
FPS = 120
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

running = True

polygon={
    "points":[], #in order
    "lignes":[],
    "triangles":[] 
}

def intriangle(pt,p1,p2,p3):
    s=((p2[1]-p3[1])*(pt[0]-p3[0])+(p3[0]-p2[0])*(pt[1]-p3[1]))/((p2[1]-p3[1])*(p1[0]-p3[0])+(p3[0]-p2[0])*(p1[1]-p3[1]))
    t=((p3[1]-p1[1])*(pt[0]-p3[0])+(p1[0]-p3[0])*(pt[1]-p3[1]))/((p2[1]-p3[1])*(p1[0]-p3[0])+(p3[0]-p2[0])*(p1[1]-p3[1]))
    if 0<=s<=1 and 0<=t<=1 and (s+t)<=1:
        return True
    return False

def do(poly):
    polygon=copy.deepcopy(poly)
    while len(polygon["points"])>3:
        n=len(polygon["points"])
        for i in  range(n):
            p1=polygon["points"][i-2]
            p2=polygon["points"][i-1]
            p3=polygon["points"][i]
            nb=0
            for j in range(len(polygon["points"])):
                if j!=i and j!=i-1 and j!=i-2:
                    if intriangle(polygon["points"][j],p1,p2,p3):
                        nb+=1
            if nb==0:
                poly["triangles"].append((p1,p2,p3))
                del polygon["points"][i-1]
                break
    p1=polygon["points"][0]
    p2=polygon["points"][1]
    p3=polygon["points"][2]
    poly["triangles"].append((p1,p2,p3))
    return poly

while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pos1 = (pos[0]/WIDTH, pos[1]/HEIGHT)
            polygon["points"].append(pos1)
    for i in range(len(polygon["points"])):
            pygame.draw.circle(screen, (255, 255, 255), (int(polygon["points"][i][0]*WIDTH), int(polygon["points"][i][1]*HEIGHT)), 5)
            pygame.draw.line(screen, (0,255,0), (int(polygon["points"][i-1][0]*WIDTH), int(polygon["points"][i-1][1]*HEIGHT)), (int(polygon["points"][i][0]*WIDTH), int(polygon["points"][i][1]*HEIGHT)), 2)
    
    if len(polygon["points"])>=3:
        polygon=do(polygon)
        
        for i in range(len(polygon["triangles"])):
            for j in range(3):
                pygame.draw.line(screen, (0,0,255), (int(polygon["triangles"][i][j-1][0]*WIDTH), int(polygon["triangles"][i][j-1][1]*HEIGHT)), (int(polygon["triangles"][i][j][0]*WIDTH), int(polygon["triangles"][i][j][1]*HEIGHT)), 2)

    clock.tick(FPS)
    pygame.display.update()
quit()