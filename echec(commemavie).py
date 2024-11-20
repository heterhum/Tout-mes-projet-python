from p5 import *

taille=100
nb_carree=8

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

noir={}
s=taille/2
y=taille+s
for _ in range(8): #car 8 piece *2 meme si j'aggrandie y'aura pas plus de piece          
    noir[int(s),y]=[1,False]
    s+=taille

#1: pion, 2: tour, 3:chevaux,4: fou,5:reine,6:roi
s=taille/2
y=s
for i in range(8):
    if i ==0:
        noir[int(s),y]=[2,False]
    if i ==1:
        noir[int(s),y]=[3,False]
    if i ==2:
        noir[int(s),y]=[4,False]
    if i ==3:
        noir[int(s),y]=[5,False]
    if i ==4:
        noir[int(s),y]=[6,False]
    if i ==5:
        noir[int(s),y]=[4,False]
    if i ==6:
        noir[int(s),y]=[3,False]
    if i ==7:
        noir[int(s),y]=[2,False]
    s+=taille

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
    global chavalier_blanc, chavalier_noir, fou_blanc, fou_noir, pion_blanc, pion_noir, reine_noir, reine_blanc, roi_blanc, roi_noir, tour_blanc, tour_noir
    size(len(liste[0])*taille, len(liste)*taille)
    no_stroke()
    background(204)
    image_mode(CENTER)
    chavalier_blanc=load_image("Tout-mes-projet-python/img_echec/chavalier_blanc.png")
    chavalier_noir=load_image("Tout-mes-projet-python/img_echec/chavalier_noir.png")
    fou_blanc=load_image("Tout-mes-projet-python/img_echec/fou_blanc.png")
    fou_noir=load_image("Tout-mes-projet-python/img_echec/fou_noir.png")
    pion_blanc=load_image("Tout-mes-projet-python/img_echec/pion_blanc.png")
    pion_noir=load_image("Tout-mes-projet-python/img_echec/pion_noir.png")
    reine_blanc=load_image("Tout-mes-projet-python/img_echec/reine_blanc.png")
    reine_noir=load_image("Tout-mes-projet-python/img_echec/reine_noir.png")
    roi_blanc=load_image("Tout-mes-projet-python/img_echec/roi_blanc.png")
    roi_noir=load_image("Tout-mes-projet-python/img_echec/roi_noir.png")
    tour_blanc=load_image("Tout-mes-projet-python/img_echec/tour_blanc.png")
    tour_noir=load_image("Tout-mes-projet-python/img_echec/tour_noir.png")

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

    for i in blanc:
        if blanc[i][0]==1:
            image(pion_blanc,i[0],i[1],taille,taille)

run()







