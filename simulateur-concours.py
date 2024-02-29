import random

nombre_personne = 0
personne = []


continu = input("d'autre personne doivent s'inscrire ? \n").lower()
if continu == "true" :
    utilisateur_incription = input("donnez votre nom \n")
    personne.append(utilisateur_incription)
    while continu == "true":
        nombre_personne += 1
        continu = input("D'autres personnes doivent-elles s'inscrire ? \n").lower()
        if continu == "true":
            utilisateur_inscription = input("Donnez votre nom\n")
            personne.append(utilisateur_incription)

print(len(personne),personne)


