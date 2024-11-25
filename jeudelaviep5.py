from p5 import *

grille_num = [[0 for j in range(30)] for i in range(30)]
taille=30
first_grille=True
first_place=True
fps=10
tempo=[]
temposuivant=[]

def check(grille,x,y):
    cellule=grille[y][x]
    if x==len(grille)-1 or x==0 or y==len(grille[x])-1 or y==0:
        s=0
    else :
        s=grille[y-1][x-1]+grille[y-1][x]+grille[y-1][x+1]+grille[y][x-1]+grille[y][x+1]+grille[y+1][x-1]+grille[y+1][x]+grille[y+1][x+1]
    if s==3:
        return 1
    elif s==2:
        return cellule
    elif s<3 or s>=4:
        return 0
    
def createtempo(tempo,x,y):
    tempos=[]
    if (x, y) not in tempo:
        tempos.append((x, y))
    if (x - 1, y) not in tempo:
        tempos.append((x - 1, y))
    if (x + 1, y) not in tempo:
        tempos.append((x + 1, y))
    if (x + 1, y - 1) not in tempo:
        tempos.append((x + 1, y - 1))
    if (x + 1, y + 1) not in tempo:
        tempos.append((x + 1, y + 1))
    if (x - 1, y - 1) not in tempo:
        tempos.append((x - 1, y - 1))
    if (x - 1, y + 1) not in tempo:
        tempos.append((x - 1, y + 1))
    if (x, y - 1) not in tempo:
        tempos.append((x, y - 1))
    if (x, y + 1) not in tempo:
        tempos.append((x, y + 1))

    return tempos

def setup():
    size(len(grille_num[0])*taille, len(grille_num)*taille)
    


def draw():
    global first_grille,grille_num,first_place,tempo,temposuivant

    if first_grille:
        for y in range(len(grille_num)):
            for x in range(len(grille_num[0])):
                fill(255,255,255)
                rect(x*taille,y*taille,taille,taille)
        first_grille=False

    elif first_place:
        if mouse_is_pressed:
            x=int(mouse_x//taille)
            y=int(mouse_y//taille)
            fill(0,0,0)
            rect(x*taille,y*taille,taille,taille)
            grille_num[y][x]=1
            tempo+=createtempo(tempo,x,y)
    else: 
        for i in tempo:
            x,y=i
            res=check(grille_num,x,y)
            if res==1:
                fill(0,0,0)
                rect(x*taille,y*taille,taille,taille)
                temposuivant+=createtempo(temposuivant,x,y)
            else:
                fill(255,255,255)
                rect(x*taille,y*taille,taille,taille)
        print(tempo)
        tempo=temposuivant.copy()
        temposuivant=[]

def key_pressed():
    global first_place
    if key=='a':
        first_place=False


run(renderer="skia",frame_rate=1)
