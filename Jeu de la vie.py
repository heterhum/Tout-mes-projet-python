import time as t
import tkinter as tk


grille_num = [[0 for j in range(10)] for i in range(30)]
root=tk.Tk()
root.withdraw()
ask=True
size = 20
cases = {}  
damier = tk.Canvas(root,width=len(grille_num)*size, height=len(grille_num[0])*size)
damier.pack()
root.title("Jeu de la vie")


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
    
def trans(liste):
    c=[liste[i].copy() for i in range(len(liste))]
    for i in range(len(c)):
        for e in range(len(c[0])):
            if i==len(c)-1 or i==0 or e==len(c[i])-1 or e==0:
                c[i][e]="🟥"               
            elif c[i][e]==0:
                c[i][e]="⬛"
            else:
                c[i][e]="⬜"
            
    for i in range(len(c)):
        c[i]=" ".join(c[i])

    return c

def grille_canvas(grille):
    for i in range(len(grille)):
        for e in range(len(grille[0])):
            if grille[i][e]==0:

                x0, y0 = i * size, e * size
                x1, y1 = x0 + size, y0 + size
                damier.create_rectangle(x0, y0, x1, y1, fill='white')
                      

            else:
                x0, y0 = i * size, e * size
                x1, y1 = x0 + size, y0 + size
                damier.create_rectangle(x0, y0, x1, y1, fill='black')
    return
                
def main():
    global grille_num
    #Modifie la liste pour la prochaine gen
    z=[grille_num[i].copy() for i in range(len(grille_num))]
    for i in range(len(grille_num)):
        for e in range(len(grille_num[0])):
            z[i][e]=check(grille_num,i,e)
    grille_num=z
    #grille_num_main est la nouvelle génération

    #prend la liste et la mais sous sa forme graphique
    grille_canvas(grille_num)
    root.after(1000,main)


#Avant tout savoir si l'user veut ajouté des cellules manuellement
while ask:
    n=input("entré une cellule ? [Y,N] ")
    if n=="Y":
        x,y=int(input("position x: ")),int(input("position y: "))
        grille_num[x][y]=1
    else:
        ask=False    

root.deiconify()

main()

root.mainloop()




    



    #if (i, j) in cases:  # si la case existe...
    #    return
    #damier.bind('<1>', on_click)