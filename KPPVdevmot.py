from math import sqrt
from tqdm.auto import tqdm

print("démmare")

file  = open("mots.txt","r",encoding="utf8")
lignes = file.readlines()
lignes=[l.strip('\n\r') for l in lignes]
l=[]
dico=[]
for i in lignes:
    dico.append("mot"+"-"+i)
    for j in range(30):
        if 0<=j<len(i):
            match i[j]:
                case "a": dico.append(i[j]+"02")
                case "b": dico.append(i[j]+"04")
                case "c": dico.append(i[j]+"06")
                case "d": dico.append(i[j]+"08")
                case "e": dico.append(i[j]+"10")
                case "f": dico.append(i[j]+"12")
                case "g": dico.append(i[j]+"14")
                case "h": dico.append(i[j]+"016")
                case "i": dico.append(i[j]+"018")
                case "j": dico.append(i[j]+"020")
                case "k": dico.append(i[j]+"022")
                case "l": dico.append(i[j]+"024")
                case "m": dico.append(i[j]+"026")
                case "n": dico.append(i[j]+"028")
                case "o": dico.append(i[j]+"030")
                case "p": dico.append(i[j]+"032")
                case "q": dico.append(i[j]+"034")
                case "r": dico.append(i[j]+"036")
                case "s": dico.append(i[j]+"038")
                case "t": dico.append(i[j]+"040")
                case "v": dico.append(i[j]+"042")
                case "w": dico.append(i[j]+"044")
                case "x": dico.append(i[j]+"046")
                case "y": dico.append(i[j]+"048")
                case "z": dico.append(i[j]+"050")
                case "â": dico.append(i[j]+"052")
                case "à": dico.append(i[j]+"054")
                case "ç": dico.append(i[j]+"056")
                case "é": dico.append(i[j]+"058")
                case "è": dico.append(i[j]+"060")
                case "-": dico.append(i[j]+"064")
                case "î": dico.append(i[j]+"066")
                case "û": dico.append(i[j]+"068")
                case "u": dico.append(i[j]+"070")
                case "ù": dico.append(i[j]+"071")
                case "ê": dico.append(i[j]+"072")
                case "ô": dico.append(i[j]+"073")
                case "ä": dico.append(i[j]+"074")
                case "ë": dico.append(i[j]+"075")
                case "ï": dico.append(i[j]+"076")
                case "ö": dico.append(i[j]+"077")
                case "ü": dico.append(i[j]+"078")
                case "ÿ": dico.append(i[j]+"079")
                case _: dico.append(i[j]+"080")
        else:
            dico.append(" "+"62")
    dico.append('0')
    l.append(dico)
    dico=[]

print("démmare kppv")

def distance_euclidienne(d2,d1):
    d2[-1]=int(d2[-1])
    b=list(zip(d1,d2))
    for i in range(1,30):
            d2[-1]+=(int(b[i][1][1:])-int(b[i][0][1:]))**2
    d2[-1]=sqrt(int(d2[-1]))
    return d2  

def table_avec_distances(donnees, cible):
    for i in tqdm(range(len(donnees))):
        
        d=distance_euclidienne(donnees[i],cible)
        donnees[i]=d
    return donnees

def tri_distance(d):
    d=sorted(d, key=lambda x: x[0])
    return d


def kppv(donnees, cible, k):    
    distances_voisins = table_avec_distances(donnees,cible)
    
    distances_voisins_triee = tri_distance(distances_voisins)

    k_plus_proches_voisins = distances_voisins_triee[:k]
    
    return k_plus_proches_voisins

mot="mat"
dico=[]
dico.append("mot"+"-"+mot)
for j in range(30):
    if 0<=j<len(mot):
        match i[j]:
            
            case "a": dico.append(i[j]+"02")
            case "b": dico.append(i[j]+"04")
            case "c": dico.append(i[j]+"06")
            case "d": dico.append(i[j]+"08")
            case "e": dico.append(i[j]+"10")
            case "f": dico.append(i[j]+"12")
            case "g": dico.append(i[j]+"14")
            case "h": dico.append(i[j]+"016")
            case "i": dico.append(i[j]+"018")
            case "j": dico.append(i[j]+"020")
            case "k": dico.append(i[j]+"022")
            case "l": dico.append(i[j]+"024")
            case "m": dico.append(i[j]+"026")
            case "n": dico.append(i[j]+"028")
            case "o": dico.append(i[j]+"030")
            case "p": dico.append(i[j]+"032")
            case "q": dico.append(i[j]+"034")
            case "r": dico.append(i[j]+"036")
            case "s": dico.append(i[j]+"038")
            case "t": dico.append(i[j]+"040")
            case "v": dico.append(i[j]+"042")
            case "w": dico.append(i[j]+"044")
            case "x": dico.append(i[j]+"046")
            case "y": dico.append(i[j]+"048")
            case "z": dico.append(i[j]+"050")
            case "â": dico.append(i[j]+"052")
            case "à": dico.append(i[j]+"054")
            case "ç": dico.append(i[j]+"056")
            case "é": dico.append(i[j]+"058")
            case "è": dico.append(i[j]+"060")
            case "-": dico.append(i[j]+"064")
            case "î": dico.append(i[j]+"066")
            case "û": dico.append(i[j]+"068")
    else:
        dico.append(" "+"62")



c=kppv(l,dico,3)
print("mot cherché : ",  mot)
print("mot trouvé : ")
for i in c:
    print(i[0][4:])