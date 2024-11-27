from p5 import *

LARGEUR=500
HAUTEUR=500
ITERATION=500
ni=0

def setup():
    size(LARGEUR,HAUTEUR)
    no_loop()
    

def draw():
    global ni
    for y in range(HAUTEUR):
        for x in range(LARGEUR):
            n=0
            zn=0
            zn1=zn**2+(x+y)
            zn+=1
            while zn1<2 and n<ITERATION:
                zn1=zn**2+(zn1)
                zn+=1
                n+=1
            if zn1<2:
                fill(200,200,200)
                point(x,y)
            else:
                fill(100,100,100)
                point(x,y)
            ni+=1
            print(ni)
run()