class moove:
    def __init__(self,n):
        self.n=n
        self.Mchavalier=[(1,-2),(2,-1),(-1,-2),(-2,-1),(-1,+2),(-2,1),(1,2),(2,1)]
        self.Mtour=[[(i,0) for i in range(1,n)],[(0,i) for i in range(1,n)],[(-i,0) for i in range(1,n)],[(0,-i) for i in range(1,n)]]

    def chavalier(self,act,dicon,dicob,col):
        lstM=[]
        xi=act[0]
        yi=act[1]
        for i in self.Mchavalier:
            x,y=i
            
            if 0<=x+xi<self.n and 0<=y+yi<self.n:
                print(i,x,y,xi,yi)
                lstM.append((x+xi,y+yi))
         
        if col =="chavalier_blanc":
            for i in lstM:
                if i in dicob:
                    lstM.remove(i)

        if col =="chavalier_noir":
            for i in lstM:
                if i in dicon:
                    lstM.remove(i)
        return lstM
    def tour(self,act,dicon,dicob,col):
        lstM=[]
        xi=act[0]
        yi=act[1]
        test=True
        
        if col=="tour_blanc":
            for i in range(len(self.Mtour)):
                j=0
                while test:
                    print(i,j)
                    x,y=self.Mtour[i][j]
                    if 0<=x+xi<self.n and 0<=y+yi<self.n:
                        if (x+xi,y+yi) in dicob:
                            self.Mtour[i]=self.Mtour[i][:j]
                            lstM.append(self.Mtour[i])
                            test=False
                        if (x+xi,y+yi) in dicon:
                            self.Mtour[i]=self.Mtour[i][:j+1]
                            lstM.append(self.Mtour[i])
                            test=False
                    else:
                        self.Mtour[i]=self.Mtour[i][:j]
                        lstM.append(self.Mtour[i])
                        test=False
                    j+=1
        return lstM
    def move_pion(self,pos):
        self.move=[]
        x=pos[0]
        y=pos[1]
        for _ in range(2):
            y=y-self.taille
            self.move.append((x,y))
        return self.move
    
#dico blanc dico noir coordonnée
       

