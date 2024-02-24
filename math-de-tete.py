import random
import time

start_time = time.time() #prise du temps au démmarage

def choix() :
    opération = ['*','-','+'] #définie une liste d'opérateur
    a = random.randint(1, 300) #choisie un nombre aléatoire 
    b = random.randint(1, 300) 
    opérateur = random.choice(opération) #choisie un opérateur aléatoire de la liste définie avant
    return a, b, opérateur
a, b, opérateur = choix()

while a < b and opérateur == '-' :
    a, b, opérateur = choix()

valeur_utilisateur = int(input(f'{a} {opérateur} {b} =\n')) #demande a l'utilisateur de rentré une valeur en ayant prit soin de mettre ce qu'on demande avant en int et faire un retour a la ligne avec \n

temps_passé = time.time() - start_time #prend la temps écoulé aprés la réponse de l'utilisateur

resultat = eval(f'{a} {opérateur} {b}') #definie le résultat attendue

if valeur_utilisateur == resultat:                   #vérifie si la valeur entré est la meme que le résultat si oui alors il donne le temps et marque vrai sinon il marque faux
    print(True)
    print (f"Temps passé : {temps_passé:.2f} secondes") 
else:
    print(False)
    print(resultat)
    print (f"Temps passé : {temps_passé:.2f} secondes") 



