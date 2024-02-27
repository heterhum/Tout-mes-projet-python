import random

nombre_repete_par_ordi = 0 #mise en place de chaque variable
a = 0
b = 0

a = int(input("choisix l'étendue début: \n")) #demande l'étendue 
b = int(input("choisix l'étendue fin: \n"))

decompte_des_nombre ={i: 0 for i in range(a, b + 1)} #crée le dictionnaire qui sera des nombre comprit entre a et b, b inclue

def choixal():                                #génération d'un nombre aléatoire entre a et b, b inclue
    nombre_aleatoire = random.randint(a,b)
    return nombre_aleatoire                   #permet l'accès a cette variable a la suite du programme

utilisateur_choix = int(input("choisi le nombre de fois que tu veut que ce soit répété : \n"))         #nombre de fois ou le tout sera répété

while nombre_repete_par_ordi < utilisateur_choix :         #tant que le programme ne la pas répété le meme nombre de fois demandé il choisie un nombre aléatoire, il ajoute 1 au nombre de fois ou
    nombre_aleatoire = choixal()                           #le programme c'est répété et ajoute 1 a la valeur correspondant au nombre aléatoire choisie
    nombre_repete_par_ordi = nombre_repete_par_ordi + 1
    decompte_des_nombre[nombre_aleatoire] += 1
else :
    for clé, valeur in decompte_des_nombre.items() :
        pourcentage = (valeur/utilisateur_choix)*100
        print(f"{clé} est apparue {valeur} fois avec un pourcentage de {round(pourcentage,2)} %" )
    print(f"pour un total de {utilisateur_choix}")
      


    



