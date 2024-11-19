#from p5 import *
#
#taille=100
#liste=[]
#x=[0,1,0,1,0,1,0,1]
#for i in range(8):
#    liste+=[x]
#    x.reverse()
#    x=x.copy()
#
#print(liste)
#
#def setup():
#    size(len(liste[0])*taille, len(liste)*taille)
#    no_stroke()
#    background(204)
#
#def draw():
#    for y in range(len(liste)):
#        for x in range(len(liste[0])):
#            if liste[y][x]==1:
#                fill(255,255,255)
#                rect(x*taille,y*taille,taille,taille)
#            else:
#                fill(100,100,100)
#                rect(x*taille,y*taille,taille,taille)
#
#run()

size=100
s=size/2

x1=[]
def desplat(taille):
    x1=[]
    liste1=[]
    
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
        print(x1)
        
    print(liste1)

desplat(3)
blanc={

}





