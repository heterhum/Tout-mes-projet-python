from p5 import *

grille_num = [[0 for j in range(30)] for i in range(30)]
taille=30
first=True

def check(grille,x,y):
    cellule=grille[x][y]
    if x==len(grille)-1 or x==0 or y==len(grille[x])-1 or y==0:
        s=0
    else :
        s=grille[x-1][y-1]+grille[x-1][y]+grille[x-1][y+1]+grille[x][y-1]+grille[x][y+1]+grille[x+1][y-1]+grille[x+1][y]+grille[x+1][y+1]
    if s==3:
        return 1
    elif s==2:
        return cellule
    elif s<3 or s>=4:
        return 0
    
def setup():
    size(len(grille_num[0])*taille, len(grille_num)*taille)
    frame_rate(10.0)
    

def draw():
    global first,grille_num
    tempo=[]
    if first:
        for y in range(len(grille_num)):
            for x in range(len(grille_num[0])):
                fill(0,100,0)
                rect(x*taille,y*taille,taille,taille)
        first=False
    if mouse_is_pressed:
        x=mouse_x//taille
        y=mouse_y//taille
        fill(0,0,0)
        rect(x*taille,y*taille,taille,taille)
        print(x,y,len(grille_num),len(grille_num[0]))
        grille_num[int(y)][int(x)]=1

run()
