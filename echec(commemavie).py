from p5 import *
from echec_move import *

taille=100
nb_carree=8
blanche=blanche(taille)

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

first_time=True

def setup():
    global chavalier_blanc, chavalier_noir, fou_blanc, fou_noir, pion_blanc, pion_noir, reine_noir, reine_blanc, roi_blanc, roi_noir, tour_blanc, tour_noir, blanc, noir
    size(len(liste[0])*taille, len(liste)*taille)
    no_stroke()
    background(204)

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

    blanc={}
    s=taille/2
    y=taille*nb_carree-100-s
    for _ in range(8): #car 8 piece *2 meme si j'aggrandie y'aura pas plus de piece          
        blanc[int(s),y]=[pion_blanc,False]
        s+=taille
    #1: pion, 2: tour, 3:chevaux,4: fou,5:reine,6:roi
    s=taille/2
    y=taille*nb_carree-s
    for i in range(8):
        if i ==0:
            blanc[int(s),y]=[tour_blanc,False]
        if i ==1:
            blanc[int(s),y]=[chavalier_blanc,False]
        if i ==2:
            blanc[int(s),y]=[fou_blanc,False]
        if i ==3:
            blanc[int(s),y]=[reine_blanc,False]
        if i ==4:
            blanc[int(s),y]=[roi_blanc,False]
        if i ==5:
            blanc[int(s),y]=[fou_blanc,False]
        if i ==6:
            blanc[int(s),y]=[chavalier_blanc,False]
        if i ==7:
            blanc[int(s),y]=[tour_blanc,False]
        s+=taille

    noir={}
    s=taille/2
    y=taille+s
    for _ in range(8):       
        noir[int(s),y]=[pion_noir,False]
        s+=taille
    s=taille/2
    y=s
    for i in range(8):
        if i ==0:
            noir[int(s),y]=[tour_noir,False]
        if i ==1:
            noir[int(s),y]=[chavalier_noir,False]
        if i ==2:
            noir[int(s),y]=[fou_noir,False]
        if i ==3:
            noir[int(s),y]=[reine_noir,False]
        if i ==4:
            noir[int(s),y]=[roi_noir,False]
        if i ==5:
            noir[int(s),y]=[fou_noir,False]
        if i ==6:
            noir[int(s),y]=[chavalier_noir,False]
        if i ==7:
            noir[int(s),y]=[tour_noir,False]
        s+=taille

def draw():
    global first_time
    z=[]
    if first_time:
        #init echequier
        for y in range(len(liste)):
            for x in range(len(liste[0])):
                if liste[y][x]==1:
                    fill(228,202,157)
                    rect(x*taille,y*taille,taille,taille)
                else:
                    fill(193,145,73)
                    rect(x*taille,y*taille,taille,taille)

        for i in blanc:
            x=float(i[0])-taille/2
            y=float(i[1])-taille/2
            image(blanc[i][0],x,y)

        for i in noir:
            x=float(i[0])-taille/2
            y=float(i[1])-taille/2
            image(noir[i][0],x,y)
        first_time=False

    if mouse_is_pressed:
        print(mouse_x,mouse_y)
        fill("Pink")
        x1=mouse_x//taille*taille+taille/2
        y1=mouse_y//taille*taille+taille/2
        if (x1,y1) in blanc:
            if blanc[(x1,y1)][0]==pion_blanc and blanc[(x1,y1)][1]==False:
                z=blanche.move_pion((x1,y1))
                blanc[(x1,y1)][1]=True
                for i in z:
                    x=float(i[0])-taille/2
                    y=float(i[1])-taille/2
                    fill(255,255,255)
                    rect(x,y,taille,taille)
            elif blanc[(x1,y1)][0]==pion_blanc:
                z=blanche.move_pion((x1,y1))
                x=float(z[0][0])-taille/2
                y=float(z[0][1])-taille/2
                fill(0,0,0)
                rect(x,y,taille,taille)
run(renderer='skia')