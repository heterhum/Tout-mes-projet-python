class jeu:
    def __init__(self,x,y,nombre):
        self.n=1
        self.l=[]
        self.nombre=nombre
        for i in range(y):
            self.l.append([])
        for i in self.l:
            for _ in range(x):
              i.append(' ')

        self.last=0

    def joue(self,symbole):
        for i in self.l: 
            if i[self.n]==' ':
                i[self.n]=symbole
                self.last=self.l.index(i)
                return True
        return False

    def diago(self,symbole):
        for i in range(1,self.nombre):
            if self.l[self.last+i][self.n+i]==symbole:
                pass
            elif self.l[self.last+i][self.n-i]==symbole:
                pass
            elif self.l[self.last-i][self.n+i]==symbole:
                pass
            elif self.l[self.last-i][self.n-i]==symbole:
                pass
            else:
                return False
        return True
    
    def ligne(self,symbole):
        for i in range(1,self.nombre):
            if self.l[self.last+i][self.n]==symbole:
                pass
            elif self.l[self.last-i][self.n]==symbole:
                pass
            elif self.l[self.last][self.n+i]==symbole:
                pass
            elif self.l[self.last][self.n-i]==symbole:
                pass
            else:
                return False
        return True

    def check(self,symbole):
        if a.diago(symbole) or a.ligne(symbole):
            print(symbole,"win")
            return False
        else:
            return True

x,y,t=int(input("taille du tableau X : ")),int(input("taille du tableau Y : ")),int(input("nombre de jeton a alligné : "))

a=jeu(x,y,t)        
c=0
symbole=''

while a.check(symbole):
    joueur=int(input("que joué vous : "))
    a.n=joueur-1
    if c%2==0:
        symbole="X"
    else:
        symbole="O"
    a.joue(symbole)
    c+=1
    for i in reversed(a.l): print(i)