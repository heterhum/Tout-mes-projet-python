class blanche:
    def __init__(self,taille):
        self.move=[]
        self.taille=taille

    def move_pion(self,pos):
        self.move=[]
        x=pos[0]
        y=pos[1]
        for _ in range(2):
            y=y-self.taille
            self.move.append((x,y))
        return self.move
    
#dico blanc dico noir coordonnée
       

