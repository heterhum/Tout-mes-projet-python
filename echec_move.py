class moove:
    def __init__(self,n,dicon,dicob):
        self.n=n
        self.dicon=dicon
        self.dicob=dicob
        self.Mchavalier=[(1,-2),(2,-1),(-1,-2),(-2,-1),(-1,+2),(-2,1),(1,2),(2,1)]
        self.Mtour=[[(i,0) for i in range(1,n)],[(0,i) for i in range(1,n)],[(-i,0) for i in range(1,n)],[(0,-i) for i in range(1,n)]]
        self.Mfou=[[(i,i) for i in range(1,n)],[(-i,-i) for i in range(1,n)],[(-i,i) for i in range(1,n)],[(i,-i) for i in range(1,n)]]
        self.Mreine=[[(i,0) for i in range(1,n)],[(0,i) for i in range(1,n)],[(-i,0) for i in range(1,n)],[(0,-i) for i in range(1,n)],[(i,i) for i in range(1,n)],[(-i,-i) for i in range(1,n)],[(-i,i) for i in range(1,n)],[(i,-i) for i in range(1,n)]]
        self.Mroi=[(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
        self.Mpionb=[[(0,-1),(0,-2)],[(-1,-1),(1,-1)]]
        self.Mpionn=[[(0,1),(0,2)],[(-1,1),(1,1)]]

    def idkthename(self,act,something,col):
        print(act,col)
        lstM=[]
        xi=act[0]
        yi=act[1]
        if col=="blanc":
            print(something,print(self.Mfou))
            for i in range(len(something)):
                j=0
                test=True
                while test:
                    print(i,j)
                    x,y=something[i][j]
                    if 0<=x+xi<self.n and 0<=y+yi<self.n:
                        if (x+xi,y+yi) in self.dicob:
                            something[i]=something[i][:j]
                            lstM.append(something[i])
                            test=False
                        if (x+xi,y+yi) in self.dicon:
                            something[i]=something[i][:j+1]
                            lstM.append(something[i])
                            test=False
                        
                    else:
                        something[i]=something[i][:j]
                        lstM.append(something[i])
                        test=False
                    j+=1
            
        elif col=="noir":
            for i in range(len(something)):
                j=0
                test=True
                while test:
                    x,y=something[i][j]
                    if 0<=x+xi<self.n and 0<=y+yi<self.n:
                        if (x+xi,y+yi) in self.dicon:
                            something[i]=something[i][:j]
                            lstM.append(something[i])
                            test=False
                        if (x+xi,y+yi) in self.dicob:
                            something[i]=something[i][:j+1]
                            lstM.append(something[i])
                            test=False
                    else:
                        something[i]=something[i][:j]
                        lstM.append(something[i])
                        test=False
                    j+=1
        return lstM
    
    def chavalier(self,act,col):
        lstM=[]
        xi=act[0]
        yi=act[1]
        for i in self.Mchavalier:
            x,y=i
            
            if 0<=x+xi<self.n and 0<=y+yi<self.n:
                
                lstM.append((x+xi,y+yi))
         
        if col =="chavalier_blanc":
            for i in lstM:
                if i in self.dicob:
                    lstM.remove(i)

        if col =="chavalier_noir":
            for i in lstM:
                if i in self.dicon:
                    lstM.remove(i)
        return lstM
    
    def tour(self,act,col):
        lstM=[]
        xi=act[0]
        yi=act[1]
        
        if col=="tour_blanc":
            lstMi=self.idkthename(act,self.Mtour,"blanc")

        elif col=="tour_noir":
            lstMi=self.idkthename(act,self.Mtour,"noir")

        for i in lstMi:
            if i:
                for j in i:
                    x,y=j
                    lstM.append((x+xi,y+yi))
        return lstM
    
    def fou(self,act,col):
        lstM=[]
        xi=act[0]
        yi=act[1]
        
        if col=="fou_blanc":
            lstMi=self.idkthename(act,self.Mfou,"blanc")

        elif col=="fou_noir":
            lstMi=self.idkthename(act,self.Mfou,"noir")

        for i in lstMi:
            if i:
                for j in i:
                    x,y=j
                    lstM.append((x+xi,y+yi))
        return lstM

    def reine(self,act,col):
        lstM=[]
        xi=act[0]
        yi=act[1]
        
        if col=="reine_blanc":
            lstMi=self.idkthename(act,self.Mreine,"blanc")

        elif col=="reine_noir":
            lstMi=self.idkthename(act,self.Mreine,"noir")

        for i in lstMi:
            if i:
                for j in i:
                    x,y=j
                    lstM.append((x+xi,y+yi))
        return lstM

    def roi(self,act,col,alle):
        lstM=[]
        xi=act[0]
        yi=act[1]
        for i in self.Mroi:
            x,y=i
            
            if 0<=x+xi<self.n and 0<=y+yi<self.n:
                
                lstM.append((x+xi,y+yi))
         
        if col =="roi_blanc":
            for i in lstM:
                if i in self.dicob or (i in alle):
                    lstM.remove(i)

        if col =="roi_noir":
            for i in lstM:
                if i in self.dicon or (i in alle):
                    lstM.remove(i)
        return lstM
    
    def pion(self,act,col,Fmove=False):
        lstM=[]
        xi=act[0]
        yi=act[1]
        if col=="pion_blanc":
            for i in self.Mpionb[0]:
                x,y=i
                if 0<=x+xi<self.n and 0<=y+yi<self.n and ((x+xi,y+yi)not in (self.dicob or self.dicon)):
                    
                    lstM.append((x+xi,y+yi))
            if Fmove: lstM.pop()
            for i in self.Mpionb[1]:
                x,y=i
                if ((x+xi,y+yi)) in self.dicon:
                    lstM.append((x+xi,y+yi))
         
        if col=="pion_noir":
            for i in self.Mpionn[0]:
                x,y=i
                if 0<=x+xi<self.n and 0<=y+yi<self.n and ((x+xi,y+yi)not in (self.dicob or self.dicon)):
                    
                    lstM.append((x+xi,y+yi))
            if Fmove: lstM.pop()
            for i in self.Mpionb[1]:
                x,y=i
                if ((x+xi,y+yi)) in self.dicob:
                    lstM.append((x+xi,y+yi))


        return lstM
    
    def Allmoove(self,act,col,Fmove=False):
        alle1=[]
        alle=[]
        match col:
            case "chavalier_noir": return self.chavalier(act,col)
            case "chavalier_blanc":return self.chavalier(act,col)
            case "fou_noir": return self.fou(act,col)
            case "fou_blanc": return self.fou(act,col)
            case "tour_noir": return self.tour(act,col)
            case "tour_blanc": return self.tour(act,col)
            case "pion_noir": return self.pion(act,col,Fmove)
            case "pion_blanc": return self.pion(act,col,Fmove)
            case "reine_noir": return self.reine(act,col)
            case "reine_blanc": return self.reine(act,col)
            case "roi_noir":
                for cle,valeur in self.dicob.items():
                    if valeur[1]!="roi_noir" or "roi_noir":
                        alle1+=self.Allmoove(cle,valeur[1],valeur[2])
                for j in alle1:
                    alle+=[i for i in j]
                return self.roi(act,col,alle)
            case "roi_blanc": return self.roi(act,col)

