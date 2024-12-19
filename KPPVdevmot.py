#from math import sqrt
from tqdm.auto import tqdm

print("démmare")

file  = open("mots.txt","r",encoding="utf8")
lignes = file.readlines()
lignes=[l.strip('\n\r') for l in lignes]

mot="ortografe"
trie=[]

for i in tqdm(lignes):
    s=len(i)-len(mot)
    n=len(i)
    c=[]
    for k in range(n):
        z=list(zip(i,mot))
        for j in z:
            if j[0]!=j[1]:
                s+=1
        if s>=0:
            c.append(s)
    s=len(i)-len(mot)
    for k in range(n):
        d=i
        d=list(d)
        d.insert(k,' ')
        z=list(zip(d,mot))
        for j in z:
            if j[0]!=j[1]:
                s+=1
        if s>=0: 
            c.append(s)
    if c!=[]:
        c=sorted(c)[0]
        trie.append([i,c])

trie=sorted(trie, key=lambda x: x[1])
print(trie[:5])