from p5 import *

taillex=10
tailley=10
grille_num = [[0 for j in range(taillex)] for i in range(tailley)]
taille=50
first_grille=True
first_place=True
fps=10
tempo=[]
temposuivant=[]

def valide(x,y):
    if x<0 or y<0:
        raise(TypeError)
    return x,y

def valide2(x,y):
    if not 0<x<taillex-1 or (not 0<y<tailley-1):
        return False
    return True

def check(grille,x,y):
    cellule=grille[y][x]
    s=0
    try:
        a,b=valide(y-1,x-1)
        s+=grille[a][b]
    except: pass

    try:
        a,b=valide(y-1,x)
        s+=grille[a][b]
    except: pass

    try:
        a,b=valide(y-1,x+1)
        s+=grille[a][b]
    except: pass

    try:
        a,b=valide(y,x+1)
        s+=grille[a][b]
    except: pass

    try:
        a,b=valide(y,x-1)
        s+=grille[a][b]
    except: pass

    try:
        a,b=valide(y+1,x-1)
        s+=grille[a][b]
    except: pass
    try:
        a,b=valide(y+1,x)
        s+=grille[a][b]
    except: pass
    try:
        a,b=valide(y+1,x+1)
        s+=grille[a][b]
    except: pass

    if s==3:
        return 1
    elif s==2:
        return cellule
    elif s<3 or s>=4:
        return 0
    
def createtempo(tempoa,x,y):
    tempos=[]
    if (x, y) not in tempoa and valide2(x,y):
        tempos.append((x, y))
    if (x - 1, y) not in tempoa and valide2(x,y):
        tempos.append((x - 1, y))
    if (x + 1, y) not in tempoa and valide2(x,y):
        tempos.append((x + 1, y))
    if (x + 1, y - 1) not in tempoa and valide2(x,y):
        tempos.append((x + 1, y - 1))
    if (x + 1, y + 1) not in tempoa and valide2(x,y):
        tempos.append((x + 1, y + 1))
    if (x - 1, y - 1) not in tempoa and valide2(x,y):
        tempos.append((x - 1, y - 1))
    if (x - 1, y + 1) not in tempoa and valide2(x,y):
        tempos.append((x - 1, y + 1))
    if (x, y - 1) not in tempoa and valide2(x,y):
        tempos.append((x, y - 1))
    if (x, y + 1) not in tempoa and valide2(x,y):
        tempos.append((x, y + 1))

    return tempos

def setup():
    size(taillex*taille+(taille*taillex/2), tailley*taille)
    background(240)

def draw():
    global first_grille,grille_num,first_place,tempo,temposuivant
    nul=[]
    posi=[]

    if first_grille:
        for y in range(tailley):
            for x in range(taillex):
                fill(255,255,255)
                rect(x*taille,y*taille,taille,taille)
        first_grille=False
        print("fait")

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
                posi.append((x,y))
                temposuivant+=createtempo(temposuivant,x,y)
            else:
                fill(255,255,255)
                rect(x*taille,y*taille,taille,taille)
                nul.append((x,y))
        for i in posi:
            grille_num[i[1]][i[0]]=1
        for i in nul:
            grille_num[i[1]][i[0]]=0
        tempo=temposuivant.copy()
        temposuivant=[]

def key_pressed():
    global first_place
    if key=='a':
        first_place=False
        fill(100,200,66)
        textSize(3*taille)
        text("Génération : ",(taillex+1)*taille,(tailley/5)*taille)

run(renderer="skia",frame_rate=10)