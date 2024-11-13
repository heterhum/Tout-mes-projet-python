import random

a = int(input("choisix l'étendue début: \n")) 
b = int(input("choisix l'étendue fin: \n"))
utilisateur_choix = int(input("choisi le nombre de fois que tu veut que ce soit répété : \n"))  

decompte_des_nombre ={i: [0,0] for i in range(a, b + 1)} 
                       
def pourcentage():
    for i in decompte_des_nombre:
        decompte_des_nombre[i][1]=int(decompte_des_nombre[i][0]/utilisateur_choix*100)
    return

for _ in range(utilisateur_choix):                          
    decompte_des_nombre[random.randint(a,b)][0]+=1
    
pourcentage()

print(decompte_des_nombre)   
