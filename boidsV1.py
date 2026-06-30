import pygame
import numpy as np
import random as rd
import copy
 
TAILLEX=1200
TAILLEY=800

screen = pygame.display.set_mode((TAILLEX,TAILLEY))
clock=pygame.time.Clock()
running=True
FPS=30

pygame.init()


def RandomVecN():
    r=rd.random()
    r=round(r,2)
    y=np.sqrt(1-r**2)
    return np.array([r*rd.choice([-1,1]),y*rd.choice([-1,1])])

def normalise(vect):
    norm = np.linalg.vector_norm(vect)
    if norm > 1e-8:
        return vect / norm
    return np.array([0.0,0.0])

class Pigeon:
    def __init__(self):
        self.NumberPig=150
        self.NumberEat=2
        self.ListPig={}
        self.ListEat={}

        self.Will=1
        self.SeparationFactor=140
        self.AlignmentFactor=20
        self.CohesionFactor=1
        self.EatFactor=12

        self.Vision=10
        self.EatVision=1000

    def CreatePig(self):
        for i in range(self.NumberPig):
            self.ListPig[i]={
                "pos":np.array([rd.randint(0,TAILLEX),rd.randint(0,TAILLEY)]),
                "vit":30,
                "vecDir": np.array([0.0,0.0]),
                "vecSpeed":np.array([0.0,0.0]),
                "vision":self.Vision, #if all same vision -> optimisation nieghPIg
                "sep":1,
                "neigh":[],
                "tosep":["n",float('inf')], #who, dist
                "Eat":["n",float('inf')],
                "EatVision":self.EatVision,
                }
        return

    def CreateEat(self):
        for i in range(self.NumberPig):
            self.ListEat[i]=np.array([rd.randint(int(TAILLEX/4),int(TAILLEX/2)),rd.randint(int(TAILLEY/4),int(TAILLEY/2))])

    def DistancePig(self,n1,n2):
        dist=np.sqrt((self.ListPig[n1]["pos"][0]-self.ListPig[n2]["pos"][0])**2 + (self.ListPig[n1]["pos"][1]-self.ListPig[n2]["pos"][1])**2)
        return dist

    def DistanceEat(self,n1,n2):
        dist=np.sqrt((self.ListPig[n1]["pos"][0]-self.ListEat[n2][0])**2 + (self.ListPig[n1]["pos"][1]-self.ListEat[n2][1])**2)
        return dist

    def NeighPig(self,old,i):
        for y in range(self.NumberPig):
            if y>i:
                d=self.DistancePig(i,y)
                if d<=old[i]["vision"]:
                    old[i]["neigh"].append(y)
                    old[y]["neigh"].append(i)
                if d<=old[i]["sep"] and d<=old[i]["tosep"][1]:
                    old[i]["tosep"][0]=y
                    old[i]["tosep"][1]=d
                    old[y]["tosep"][0]=i
                    old[y]["tosep"][1]=d
        for y in range(self.NumberEat):
            d=self.DistanceEat(i,y)
            if d<=self.EatVision and d<=old[i]["Eat"][1]:
                old[i]["Eat"][1]=d
                old[i]["Eat"][0]=y
        return

    def Separation(self,n,tosep,old): #for now only in fonction of most near 
        if tosep[0]!="n":
            pri=old[n]["pos"]
            fuire=old[tosep[0]]["pos"]
            #vec=np.array([pri[0]-fuire[0],pri[1]-fuire[1]])
            vec=pri-fuire
            Vedir=normalise(vec)

            return Vedir #direction to run from nearest pigeon
        else: return np.array([0.0,0.0])

    def Alignment(self,n,neigh,old):
        tot=np.array([0.0,0.0])
        if neigh!=[]:
            for i in neigh:
                tot+=old[i]["vecDir"]
            moy=tot/len(neigh)
            return normalise(moy) #build only with vdir, so individual pigeon speed does not impact their impact (lol), direction of where group go
        else:
            return old[n]["vecDir"]

    def Cohesion(self,n,neigh,old):
        tot=np.array([0.0,0.0])
        if neigh!=[]:
            for i in neigh:
                tot+=old[i]["pos"]
            moy=tot/len(neigh)
            v=old[n]["pos"]-moy
            return normalise(v)
        else:
            return old[n]["vecDir"]

    def Eat(self,n,eat,old):
        if eat[0]!="n":
            pri=old[n]["pos"]
            fuire=self.ListEat[eat[0]]
            vec=fuire-pri
            Vedir=normalise(vec)

            return Vedir #direction to run from nearest pigeon
        else: return np.array([0.0,0.0])

    def Mouvement(self,i):
        self.ListPig[i]["pos"]=self.ListPig[i]["pos"]+(1/FPS)*self.ListPig[i]["vecSpeed"]
        return

    def BIGPIGEON(self):
        old=copy.deepcopy(self.ListPig)
        
        for i in range(self.NumberPig):
            #if old[i]["Eat"][0]=="n" and int(old[i]["vecSpeed"][0])==0 and int(old[i]["vecSpeed"][1])==0: #badddd
            #    old[i]["vision"]=1000
            #    
            #else:
            #    old[i]["vision"]=self.Vision
            self.NeighPig(old,i)

            vd0=self.Separation(i,old[i]["tosep"],old)
            vd1=self.Alignment(i,old[i]["neigh"],old)
            vd2=self.Cohesion(i,old[i]["neigh"],old)
            vd3=self.Eat(i,old[i]["Eat"],old)
            
            vd0*=self.SeparationFactor
            vd1*=self.AlignmentFactor
            vd2*=self.CohesionFactor
            vd3*=self.EatFactor

            new=vd0+vd1+vd2+vd3
            t=new*(1/FPS)

            u=old[i]["vecSpeed"]*self.Will+t
            if np.linalg.vector_norm(u)>old[i]["vit"]:
                u=normalise(u)*old[i]["vit"]

            self.ListPig[i]["vecDir"]=normalise(u)
            self.ListPig[i]["vecSpeed"]=u

            self.ListPig[i]["neigh"]=[]
            self.ListPig[i]["tosep"]=["n",float('inf')]
            self.ListPig[i]["Eat"]=["n",float('inf')] #"n" not 0 ; it's a ~feature~

            self.Mouvement(i)
            self.Show(i)

            for y in range(self.NumberEat):
                if int(self.ListPig[i]["pos"][0])==self.ListEat[y][0] and int(self.ListPig[i]["pos"][1])==self.ListEat[y][1]:
                    self.ListEat[y]=np.array([rd.randint(int(TAILLEX/4),int(TAILLEX/2)),rd.randint(int(TAILLEY/4),int(TAILLEY/2))])

        return

    def ShowEat(self):
        for i in range(self.NumberEat):
            posx=self.ListEat[i][0]
            posy=self.ListEat[i][1]
            if 0<=posx<=TAILLEX and 0<=posy<=TAILLEY:
                #pygame.draw.circle(screen,(255,255,0),self.ListEat[i],self.EatVision)
                #pygame.draw.circle(screen,(0,0,0),self.ListEat[i],self.EatVision-1)
                pygame.draw.circle(screen,(255,255,0),self.ListEat[i],2)

    def Show(self,i):
        posx=self.ListPig[i]["pos"][0]
        posy=self.ListPig[i]["pos"][1]
        if 0<=posx<=TAILLEX and 0<=posy<=TAILLEY:
            p1=self.ListPig[i]["vecDir"]*3+self.ListPig[i]["pos"]
            p2=[self.ListPig[i]["vecDir"][1]*1+self.ListPig[i]["pos"][0],-self.ListPig[i]["vecDir"][0]*1+self.ListPig[i]["pos"][1]]
            p3=[-self.ListPig[i]["vecDir"][1]*1+self.ListPig[i]["pos"][0],self.ListPig[i]["vecDir"][0]*1+self.ListPig[i]["pos"][1]]
            #pygame.draw.circle(screen,(255,0,0),self.ListPig[i]["pos"],2)
            pygame.draw.polygon(screen,(255,0,0),[p1,p2,p3])

                


Pig=Pigeon()
Pig.CreatePig()
Pig.CreateEat()

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            Pig.ListEat[0]=np.array([pos[0],pos[1]])
    Pig.ShowEat()        
    Pig.BIGPIGEON()
    

    pygame.display.update()
    clock.tick(FPS)