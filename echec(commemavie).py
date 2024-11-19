from p5 import *

taille=100
nb_carree=8
def desplat(taille):
    x1,liste1=[],[]
    
    for i in range(taille):
        if i%2:
            x1.append(0)
        else:
            x1.append(1)

    for _ in range(taille):
        liste1.append(x1.copy())
        for i in range(len(x1)):
            if x1[i]==1:
                x1[i]=0
            else:
                x1[i]=1
        
    return liste1

liste=(desplat(nb_carree))

def setup():
    size(len(liste[0])*taille, len(liste)*taille)
    no_stroke()
    background(204)

def draw():
    for y in range(len(liste)):
        for x in range(len(liste[0])):
            if liste[y][x]==1:
                fill(255,255,255)
                rect(x*taille,y*taille,taille,taille)
            else:
                fill(100,100,100)
                rect(x*taille,y*taille,taille,taille)
    s=taille/2
    y=taille*nb_carree-100-s
    for _ in range(8):
        fill("Green")
        strokeWeight(30)
        point(s,y)
        s+=taille
    s=taille/2
    y=100+s
    for _ in range(8):
        fill("Pink")
        strokeWeight(30)
        point(s,y)
        s+=taille

run()

blanc={}
s=taille/2
y=taille*nb_carree-100-s
for _ in range(8): #car 8 piece *2 meme si j'aggrandie y'aura pas plus de piece          
    blanc[int(s),y]=[1,False]
    s+=taille

#1: pion, 2: tour, 3:chevaux,4: fou,5:reine,6:roi
s=taille/2
y=taille*nb_carree-s
for i in range(8):
    if i ==0:
        blanc[int(s),y]=[2,False]
    if i ==1:
        blanc[int(s),y]=[3,False]
    if i ==2:
        blanc[int(s),y]=[4,False]
    if i ==3:
        blanc[int(s),y]=[5,False]
    if i ==4:
        blanc[int(s),y]=[6,False]
    if i ==5:
        blanc[int(s),y]=[4,False]
    if i ==6:
        blanc[int(s),y]=[3,False]
    if i ==7:
        blanc[int(s),y]=[2,False]
    s+=taille

print(blanc)





