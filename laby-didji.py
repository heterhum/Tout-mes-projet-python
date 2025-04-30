from numpy import *
import time
import os
import copy

L,H=17,11
xS=1
yS=0
xT=15
yT=10

lab = [ ["#", "S", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", " ", " ", " ", "#", " ", "#", " ", "#", "#", " ", " ", " ", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", "#", "#", " ", "#", " ", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", " ", " ", "#", "#", " ", "#", " ", " ", " ", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", " ", "#", " ", "#", "#", "#", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", "#", " ", "#", " ", " ", " ", " ", "#", " ", "#"],
        ["#", "#", "#", " ", "#", " ", "#", "#", " ", "#", "#", "#", " ", " ", "#", " ", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
        ["#", " ", "#", " ", " ", " ", "#", "#", " ", "#", "#", "#", " ", "#", "#", " ", "#"],
        ["#", " ", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "I", "#"],
       ]

def arron(n):
    return int(round(n))
def arro(n):
    return int(round(((n)**2)**0.5))

def voisin(liste,coor,alreliste,listetraite,L,H): #voisin qui modifie
    L=len(liste[0])
    H=len(liste)
    l=[]
    xm1=coor[0]-1
    xp1=coor[0]+1
    ym1=coor[1]-1
    yp1=coor[1]+1
    chemin=coor[2]+1
    fakelist = [(t[0], t[1]) for t in alreliste]
    fakelistn=[(t[0], t[1]) for t in listetraite]

    if 0<=xm1<L:
        if liste[coor[1]][xm1] != "#"  and (xm1,coor[1]) not in fakelist and (xm1,coor[1]) not in fakelistn:
            l.append((xm1,coor[1],chemin))
    if 0<=xp1<L:
        if liste[coor[1]][xp1] != "#" and (xp1,coor[1]) not in fakelist and (xp1,coor[1]) not in fakelistn:
            l.append((xp1,coor[1],chemin))
    if 0<=ym1<H:
        if liste[ym1][coor[0]] != "#" and (coor[0],ym1) not in fakelist and (coor[0],ym1) not in fakelistn:
            l.append((coor[0],ym1,chemin))
    if 0<=yp1<H:
        if liste[yp1][coor[0]] != "#" and (coor[0],yp1) not in fakelist and (coor[0],yp1) not in fakelistn:
            l.append((coor[0],yp1,chemin))
    return l

def cherchemur(liste,coor,L,H): #voisin qui ne modifie pas, cherche les murs
    l=[]
    xm1=coor[0]-1
    xp1=coor[0]+1
    ym1=coor[1]-1
    yp1=coor[1]+1
    
    if 0<=xm1<L:
        if liste[coor[1]][xm1] == "#":
            l.append((xm1,coor[1],liste[coor[1]][xm1]))
    if 0<=xp1<L:
        if liste[coor[1]][xp1] == "#":
            l.append((xp1,coor[1],liste[coor[1]][xp1]))
    if 0<=ym1<H:
        if liste[ym1][coor[0]] == "#":
            l.append((coor[0],ym1,liste[ym1][coor[0]]))
    if 0<=yp1<H:
        if liste[yp1][coor[0]] == "#":
            l.append((coor[0],yp1,liste[yp1][coor[0]]))
    return l

def cherchevoisin(liste,coor,L,H):  #voisin qui ne modifie pas, cherche les case vides 
    l=[]
    xm1=coor[0]-1
    xp1=coor[0]+1
    ym1=coor[1]-1
    yp1=coor[1]+1
    
    if 0<=xm1<L:
        if liste[coor[1]][xm1] != "#":
            l.append((xm1,coor[1],liste[coor[1]][xm1]))
    if 0<=xp1<L:
        if liste[coor[1]][xp1] != "#":
            l.append((xp1,coor[1],liste[coor[1]][xp1]))
    if 0<=ym1<H:
        if liste[ym1][coor[0]] != "#":
            l.append((coor[0],ym1,liste[ym1][coor[0]]))
    if 0<=yp1<H:
        if liste[yp1][coor[0]] != "#":
            l.append((coor[0],yp1,liste[yp1][coor[0]]))
    return l

def place(liste,S,L,H): #donne la distance de chaque case par rapport à S
    listecheck=[]
    listefile=[]
    listefile=voisin(liste,(S[0],S[1],0),listecheck,listefile,L,H)
    listecheck.append((S[0],S[1],0))
    while len(listefile)>0:
        listecheck.append(listefile[0])
        new=voisin(liste,listefile[0],listecheck,listefile,L,H)
        listefile.pop(0)
        listefile+=new
        #time.sleep(0.5)
    return listecheck

def cherche(liste, S, T,L,H):
    lab2 = [[" " for i in range(L)] for j in range(H)]
    caseparcourue = 0
    while T!=S:
        
        listemur=cherchemur(liste,T,L,H)
        for i in listemur:
            lab2[i[1]][i[0]]="#"
        distanceparcase=place(lab2,S,L,H)
        listevoisin=cherchevoisin(lab2,T,L,H)
        for i in distanceparcase:
            lab2[i[1]][i[0]]=i[2]
        mini=listevoisin[0]
        for i in listevoisin:
            if mini[2]>i[2]:
                mini=i
        demo=copy.deepcopy(lab2)

        demo[T[1]][T[0]]="T"
        T=(mini[0],mini[1])
        caseparcourue +=1
    return caseparcourue
        
#u=cherche(lab, (xS,yS),(xT,yT),L,H)
#print(u)

import pygame

PIXEL=50
screen = pygame.display.set_mode((PIXEL*L, PIXEL*H))
running = True

def dess(grille,L,H):
    for y in range(H):
        for x in range(L):
            if grille[y][x] == "#":
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x * PIXEL, y * PIXEL, PIXEL - 1, PIXEL - 1))
            elif grille[y][x] == "S":
                pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x * PIXEL, y * PIXEL, PIXEL - 1, PIXEL - 1))
            elif grille[y][x] == "T":
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x * PIXEL, y * PIXEL, PIXEL - 1, PIXEL - 1))
            elif grille[y][x] == "@":
                pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(x * PIXEL, y * PIXEL, PIXEL - 1, PIXEL - 1))
            elif grille[y][x] == "I":
                pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(x * PIXEL, y * PIXEL, PIXEL - 1, PIXEL - 1))
            else:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x * PIXEL, y * PIXEL, PIXEL - 1, PIXEL - 1))


lab2 = [[" " for i in range(L)] for j in range(H)]
t=(xT,yT)
caseparcourue = 0
labshow = copy.deepcopy(lab)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
    #screen.fill((255, 255, 255))
    listemur=cherchemur(lab,t,L,H)
    for i in listemur:
        lab2[i[1]][i[0]]="#"
        labshow[i[1]][i[0]]="@"
    distanceparcase=place(lab2,(xS,yS),L,H)
    listevoisin=cherchevoisin(lab2,t,L,H)
    for i in distanceparcase:
        lab2[i[1]][i[0]]=i[2]
    mini=listevoisin[0]
    for i in listevoisin:
        if mini[2]>i[2]:
            mini=i
    labshow[t[1]][t[0]]="T"
    labshow[yS][xS]="S"
    t=(mini[0],mini[1])
    caseparcourue +=1

    dess(labshow,L,H)
    pygame.display.update()
    pygame.time.wait(500)
    
quit()