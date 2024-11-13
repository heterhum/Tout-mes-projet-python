import string, random, time

alphabets = list(string.ascii_letters+string.digits+string.punctuation+"é"+"à"+"è"+"ç")
print(alphabets)
target, current = "Un texte répond de façon plus ou moins pertinente à des critères qui en déterminent la qualité littéraire. On retient en particulier la structure d'ensemble, la syntaxe et la ponctuation, l'orthographe lexicale et grammaticale, la pertinence et la richesse du vocabulaire, la présence de figures de style, le registre de langue et la fonction recherchée (narrative, descriptive, expressive, argumentative, injonctive, poétique). C'est l'objet de l'analyse littéraire. ", ""
for c in target:
    letters = alphabets.copy()
    l = " "
    while l != c:
        l = random.choice(letters)
        letters.remove(l)
        print(current + l,"\r")
        time.sleep(0.009)
    current += l
