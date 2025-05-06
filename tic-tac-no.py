#overcomplicated version
X=Y=5
reussite=4
morpion=[[' ' for x in range(X)] for y in range(Y)]
m=[[' ' for x in range(X)] for y in range(Y)]
observation=[(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)]
morpion[1][1]='X'
morpion[0][0]='X'
morpion[2][2]='X'
morpion[1][0]='X'
morpion[1][1]='X'
morpion[1][2]='X'
morpion[1][3]='X'
#morpion[3][3]='X'
for i in morpion: print(i)

def dicoliste(liste,num):
    res=0
    for i in liste:
        if i["dot"]==num:
            res+=1
    return res
    

def detecte(coor,table):
    check=[]
    for i in observation:
        x1,y1=coor[0]+i[0],coor[1]+i[1]
        if 0<=x1<X and 0<=y1<Y:
            if table[y1][x1]!=' ':
                check.append((x1,y1))
            else:
                check.append(0)
        else :
            check.append(0)
    return check
        
def cherche(coor,table,symbole):
    voisin=detecte(coor,table)
    num=0
    temp=[]
    finale=[]
    visite=[]
    startnum=[]
    temp.append({"parent": None, "place":num,"liste": voisin,"dot":None,"coor":coor})
    for i in range(len(voisin)):
        if voisin[i]!=0:
            if 0<=i+4<8:
                if voisin[i+4]!=0:
                    startnum.append(i)
    
    while temp !=[] and startnum!=[]:
        act=temp[0]
        if act["dot"]==None:
            for i in range(len(act["liste"])):
                z=act["liste"][i]
                if  z !=0 and table[z[1]][z[0]]==symbole:
                    if z not in visite:
                        visite.append(act["coor"])
                        temp.append({"parent": act["coor"], "place":act["place"]+1,"liste": detecte(z,table),"dot":i,"coor":z})
                elif z !=0 and z not in visite and table[z[1]][z[0]]==symbole:
                    visite.append(act["coor"])
                    temp.append({"parent": act["coor"], "place":act["place"]+1,"liste": detecte(z,table),"dot":i,"coor":z})
                    
            finale.append(temp[0])
            temp.pop(0)
        else:
            z=act["liste"][act["dot"]]
            if z != 0 and z not in visite and table[z[1]][z[0]]==symbole:
                temp.append({"parent": act["coor"], "place":act["place"]+1,"liste": detecte(z,table),"dot":act["dot"],"coor": z})
                visite.append(act["coor"])
            finale.append(act)
            temp.pop(0)
        
    return finale,startnum
            
z=cherche((1,1),morpion,"X")
ultimatefinaleresult=[]
if z[1]!=[]:
    for i in z[1]:
        c1=dicoliste(z[0],i)
        c2=dicoliste(z[0],i+4)
        ultimatefinaleresult.append(c1+c2+1)
    if max(ultimatefinaleresult)>=reussite:
        print("win")
    else:
        print("looser")
elif z[1]==[] and len(z[0])>=reussite:
    print("win")
else:
    print("looser")


#EZ version
#X = Y = 3
#reussite = 3
#morpion = [[' ' for _ in range(X)] for _ in range(Y)]
#morpion[1][1] = 'X'
#morpion[0][0] = 'X'
#morpion[2][2] = 'X'
#
#for row in morpion:
#    print(row)
#
#def check_victoire(grille, symbole, longueur):
#    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # droite, bas, diag-bas, diag-haut
#
#    for y in range(Y):
#        for x in range(X):
#            if grille[y][x] != symbole:
#                continue
#            for dx, dy in directions:
#                count = 1
#                nx, ny = x + dx, y + dy
#                while 0 <= nx < X and 0 <= ny < Y and grille[ny][nx] == symbole:
#                    count += 1
#                    if count >= longueur:
#                        return True
#                    nx += dx
#                    ny += dy
#    return False
#
#if check_victoire(morpion, 'X', reussite):
#    print("win")
#else:
#    print("nope")