import random

nombre_personne = 0
personne = []

continu = input("tapé *oui* quand vous voudrez commencé la tombola et *non* quand vous voulez la finir\n").lower()

while continu == "oui":
    continu = input("Voulez vous vous inscrire ?\n").lower()
    if continu == "oui":
        utilisateur_inscription = input("Donnez votre nom\n")
        personne.append(utilisateur_inscription)
    elif continu != "non" :
        print("je ne comprend pas, oui ou non")
    if continu == "non" and len(personne) == 0:
        print("erreur, il semble qu'il n'y est pas de personne a tiré au sort :(")
        break
    if continu == "non":
        print("le gagnant est",random.choice(personne))
        print(f"sur : {len(personne)}\nqui sont : {personne}")
        break
