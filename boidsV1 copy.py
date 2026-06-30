import pygame
import numpy as np
import random as rd
import copy
 
TAILLEX=500
TAILLEY=500

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
        self.NumberEat=1
        self.ListPig={}
        self.ListEat={}


    def CreatePig(self):
        for i in range(self.NumberPig):
            self.ListPig[i]={
                "pos":np.array([rd.randint(0,TAILLEX),rd.randint(0,TAILLEY)]),
                "vit":rd.choice([30,50]),
                "vecDir": np.array([0.0,0.0]),
                "vecSpeed":np.array([0.0,0.0]),
                "vision":rd.choice([20,100]), #if all same vision -> optimisation nieghPIg
                "sep":1,
                "neigh":[],
                "tosep":["n",float('inf')], #who, dist
                "Eat":["n",float('inf')],
                "Will":rd.choice([1,3]),
                "SeparationFactor":rd.choice([50,140]),
                "AlignmentFactor":rd.choice([10,20]),
                "CohesionFactor":rd.choice([1,30]),
                "EatFactor":rd.choice([30,60]),
                }
        return

    def CreateEat(self):
        for i in range(self.NumberPig):
            self.ListEat[i]=np.array([rd.randint(0,TAILLEX),rd.randint(0,TAILLEY)])

    def DistancePig(self,n1,n2):
        dist=np.sqrt((self.ListPig[n1]["pos"][0]-self.ListPig[n2]["pos"][0])**2 + (self.ListPig[n1]["pos"][1]-self.ListPig[n2]["pos"][1])**2)
        return dist

    def DistanceEat(self,n1,n2):
        dist=np.sqrt((self.ListPig[n1]["pos"][0]-self.ListEat[n2][0])**2 + (self.ListPig[n1]["pos"][1]-self.ListEat[n2][1])**2)
        return dist

    def NeighPig(self):
        for i in range(self.NumberPig):
            for y in range(self.NumberPig):
                if i!=y:
                    d=self.DistancePig(i,y)
                    if d<=self.ListPig[i]["vision"]:
                        self.ListPig[i]["neigh"].append(y)
                    if d<=self.ListPig[i]["sep"] and d<=self.ListPig[i]["tosep"][1]:
                        self.ListPig[i]["tosep"][0]=y
                        self.ListPig[i]["tosep"][1]=d
            for y in range(self.NumberEat):
                d=self.DistanceEat(i,y)
                if d<=self.ListPig[i]["vision"] and d<=self.ListPig[i]["Eat"][1]:
                    self.ListPig[i]["Eat"][1]=d
                    self.ListPig[i]["Eat"][0]=y
        return

    def Separation(self,n,tosep,old): #for now only in fonction of most near 
        if tosep[0]!="n":
            pri=old[n]["pos"]
            fuire=old[tosep[0]]["pos"]
            vec=np.array([pri[0]-fuire[0],pri[1]-fuire[1]])
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
            vec=np.array([fuire[0]-pri[0],fuire[1]-pri[1]])
            Vedir=normalise(vec)

            return Vedir #direction to run from nearest pigeon
        else: return np.array([0.0,0.0])

    def Mouvement(self):
        for i in range(self.NumberPig):
            self.ListPig[i]["pos"]=self.ListPig[i]["pos"]+(1/FPS)*self.ListPig[i]["vecSpeed"]
        return

    def BIGPIGEON(self):
        self.NeighPig()
        old=copy.deepcopy(self.ListPig)
        
        for i in range(self.NumberPig):
            vd0=self.Separation(i,old[i]["tosep"],old)
            vd1=self.Alignment(i,old[i]["neigh"],old)
            vd2=self.Cohesion(i,old[i]["neigh"],old)
            vd3=self.Eat(i,old[i]["Eat"],old)
            
            vd0*=old[i]["SeparationFactor"]
            vd1*=old[i]["AlignmentFactor"]
            vd2*=old[i]["CohesionFactor"]
            vd3*=old[i]["EatFactor"]

            new=vd0+vd1+vd2+vd3
            t=new*(1/FPS)

            u=old[i]["vecSpeed"]*old[i]["Will"]+t
            if np.linalg.vector_norm(u)>old[i]["vit"]:
                u=normalise(u)*old[i]["vit"]

            self.ListPig[i]["vecDir"]=normalise(u)
            self.ListPig[i]["vecSpeed"]=u

            self.ListPig[i]["neigh"]=[]
            self.ListPig[i]["tosep"]=["n",float('inf')]
            self.ListPig[i]["Eat"]=[0,float('inf')] #"n" not 0 ; it's a ~feature~
        return

    def Show(self):
        for i in range(self.NumberEat):
            posx=self.ListEat[i][0]
            posy=self.ListEat[i][1]
            if 0<=posx<=TAILLEX and 0<=posy<=TAILLEY:
                pygame.draw.circle(screen,(255,255,0),self.ListEat[i],2)
        for i in range(self.NumberPig):
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
            
    Pig.BIGPIGEON()
    Pig.Mouvement()
    Pig.Show()

    pygame.display.update()
    clock.tick(FPS)