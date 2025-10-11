import pygame
import random as rd
import numpy as np
import time

# 10 pixels = 1m
pixel_to_m=10
WIDTH, HEIGHT = 600, 400
N=50
TAILLEX = (WIDTH // N)+1
TAILLEY = (HEIGHT // N)+1

grille=[[0 for x in range(TAILLEX)] for y in range(TAILLEY)]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 120


running = True

class Physic():
    def __init__(self):
        self.gravity=9.81 # m/s^2
        Ngravity=np.array([0,-self.gravity])
        pass

    def Vcalc(self,v,vector,x,y):
        distnace=v*(1/FPS)
        Pdistance=(distnace*pixel_to_m)
        Vx=Pdistance*vector[0]
        Vy=Pdistance*vector[1]
        x+=Vx
        y-=Vy
        return x,y
    
    def gravVcalc(self,obj):
        v=obj.velocity
        vector=obj.Vdirector
        x=obj.x
        y=obj.y
        Nvector=(vector[0]*v,vector[1]*v+(1/FPS)*(-self.gravity))
        norme=np.sqrt(Nvector[0]**2+Nvector[1]**2)
        if norme!=0:
            NewVector=(Nvector[0]/norme,Nvector[1]/norme)
        else:
            NewVector=(0,0)

        xy=self.Vcalc(norme,NewVector,x,y)
        return xy[0],xy[1],norme,NewVector
    
    def norme(self,vect):
        return np.sqrt(vect[0]**2+vect[1]**2)
    def Vnormale(self,vect,norme):
        if norme!=0:
            return (vect[0]/norme,vect[1]/norme)
        return (0,0)

    def Collimur(self,obj1,obj2): #obj1 colisionneur, obj2 mur
        Vnorm=obj2.vnorm
        dot=np.dot(obj1.Vdirector,Vnorm)*2
        tosou=(dot*Vnorm[0],dot*Vnorm[1])
        NewV=(obj1.Vdirector[0]-tosou[0],obj1.Vdirector[1]-tosou[1])

        norme=self.norme(NewV)
        NewV=self.Vnormale(NewV,norme)
        
        obj1.update(velocity=obj1.coefResti*obj1.velocity,Vdirector=NewV)
        newxy=self.gravVcalc(obj1)
        return newxy

    
    def collision(self,obj1,obj2): #obj1 colisionneur, obj2 colisionné et cercle
        Ngrav1=self.gravVcalc(obj1)
        Ngrav2=self.gravVcalc(obj2)
        obj1.update(velocity=Ngrav1[2])
        obj2.update(velocity=Ngrav2[2])
        Ec1=obj1.Ecin
        Ec2=obj2.Ecin
        m1=obj1.masse
        m2=obj2.masse

        New1=(Ngrav1[0]*Ec1,Ngrav1[1]*Ec1)
        New2=(Ngrav2[0]*Ec2,Ngrav2[1]*Ec2)

        Nvector=(New1[0]+New2[0],New1[1]+New2[1])
        norme=np.sqrt(Nvector[0]**2+Nvector[1]**2)
        v=np.sqrt(norme/(1/2*m1))
        obj1.update(velocity=v,Vdirector=(Nvector[0]/norme,Nvector[1]/norme))
        return #retourne vecteur directeur et vitesse


class circle():
    def __init__(self, x, y, r,objet):
        self.x = x
        self.y = y
        self.r = r
        self._velocity=0 # m/s
        self._masse=1 # kg
        self.coefResti=0.2 #0.83
        self._Ecin=(1/2)*self.masse*self.velocity**2
        self.Vdirector=(1,0)
        self.objectsclass=objet
        self.physic=Physic()
        self.boxPosPrec=[]
        self.updateBox()
        self.cooldown=time.time()

    def update_Ecin(self):
        self._Ecin = 0.5 * self._masse * (self._velocity ** 2)
        return

    def cooldownstart(self):
        self.cooldown=time.time()
        return
    def cooldowncheck(self):
        if time.time()-self.cooldown>=0.1:
            return True
        return False

    @property
    def Ecin(self):
        return self._Ecin
    @property
    def velocity(self):
        return self._velocity
    @property
    def masse(self):
        return self._masse
    
    @velocity.setter
    def velocity(self,v):
        self._velocity=v
        self.update_Ecin()
        return
    @masse.setter
    def masse(self,m):
        self._masse=m
        self.update_Ecin()
        return
    
    def draw(self):
        pygame.draw.circle(screen, (138, 16, 3), (self.x, self.y), self.r)
        return
    def drawVector(self): #a refaire
        pygame.draw.line(screen, (255,0,0), (self.x,self.y), (self.x+(self.Ecin*self.Vdirector[0]/10),self.y-(self.Ecin*self.Vdirector[1]/10)), width=2)
        return
    
    def update(self,x=None,y=None,r=None,velocity=None,coefResti=None,masse=None,Vdirector=None):
        if x is not None:
            self.x=x
        if y is not None:
            self.y=y
        if r is not None:
            self.r=r
        if velocity is not None:
            self.velocity=velocity  
        if coefResti is not None:
            self.coefResti=coefResti
        if masse is not None:
            self.masse=masse
        if Vdirector is not None:
            self.Vdirector=Vdirector
        return 

    def updateBox(self): #donne toute les cases occupées par le cercle
        rightTo=int((self.x+self.r)//N)
        leftTo=int((self.x-self.r)//N)
        topTo=int((self.y-self.r)//N)
        botTo=int((self.y+self.r)//N)

        lSend=[]
        for y in range(topTo,botTo+1):
            for x in range(leftTo,rightTo+1):
                lSend.append((x,y))
                self.objectsclass.addContainer(self,x,y)

        if self.boxPosPrec != []:
                for i in self.boxPosPrec:
                    if i not in lSend:
                        self.objectsclass.delContainer(id(self),i[0],i[1])
                        grille[i[1]][i[0]]=0
        self.boxPosPrec=lSend
        return 
    
    def moove(self):
        u=self.objectsclass.checkColli(self)

        newxy=self.physic.gravVcalc(self)
        x=newxy[0]
        y=newxy[1]
        self.velocity=newxy[2]
        self.Vdirector=newxy[3]
        if u != []:
            for i in u:
                uh=self.objectsclass.objectmap[i]
                if type(uh) == mur:
                    if not (0<=self.x+self.r<=WIDTH and 0<=self.y+self.r<=HEIGHT and 0<=self.x-self.r<=WIDTH and 0<=self.y-self.r<=HEIGHT) :
                        if self.cooldowncheck():
                            newxy=self.physic.Collimur(self,uh)
                            self.x=newxy[0]
                            self.y=newxy[1]
                            self.cooldownstart()
                        else:
                            self.velocity=0
                    else:
                        self.x=x
                        self.y=y
                        

                elif type(uh) == circle:
                    pass
                    #self.physic.collision(self,uh) #TO DO
                else:
                    
                    self.x=x
                    self.y=y
                    
        else:
            
            self.x=x
            self.y=y

        #if 0<=x+self.r<=WIDTH and 0<=y+self.r<=HEIGHT and 0<=x-self.r<=WIDTH and 0<=y-self.r<=HEIGHT:
        #    self.x=x
        #    self.y=y
        #    
        #else: #a tapé mur
 #
        #    
        #    self.boxPosPrec
        #    self.update(velocity=self.coefResti*self.velocity,Vdirector=(0,0))
        return

class mur():
    def __init__(self, d):
        self.d = d
        self.vnorm=self.getVector()
        self.velocity=0
        
    def getVector(self):
        if self.d == "droite":
            return (-1,0)
        if self.d == "gauche":
            return (1,0)
        if self.d == "haut":
            return (0,-1)
        if self.d == "bas":
            return (0,1)
        
    def moove(self):
        return  
    def draw(self):
        return
    def drawVector(self):
        return
    def update(self):
        return
    def updateBox(self):
        return


class objects():
    def __init__(self):
        self.objectmap={} #liste des objets présents
        self.container=[[[] for x in range(TAILLEX)] for y in range(TAILLEY)] #liste des objet dans chaque boite
        self.traceList=[]
        self.placemur()

    def placemur(self):
        droite=mur("droite")
        gauche=mur("gauche")
        haut=mur("haut")
        bas=mur("bas")
        self.addObject(droite)
        self.addObject(gauche)
        self.addObject(haut)
        self.addObject(bas)
        for y in range(TAILLEY):
            self.container[y][0].append(id(gauche))
            self.container[y][-1].append(id(droite))
        for x in range(TAILLEX):
            self.container[0][x].append(id(haut))
            self.container[-1][x].append(id(bas))
        return

    def addObject(self,obj):
        self.objectmap[id(obj)]=obj
        return id(obj)
    
    def removeObject(self,obj):
        del self.objectmap[id(obj)]
        return id(obj)
    
    def addContainer(self,obj,x,y):
        if 0<=x<TAILLEX and 0<=y<TAILLEY and id(obj) not in self.container[y][x]:
            self.container[y][x].append(id(obj))
            return True
        return False
    
    def delContainer(self,objid,x,y):
        self.container[y][x].remove(objid)
        return
    
    def trace(self,obj):
        self.traceList.append((obj.x,obj.y))

    def paintall(self):
        for i in self.objectmap.values():
            i.draw()
            i.drawVector()
            #self.trace(i)
        return
    
    def updateallBox(self):
        for i in self.objectmap.values():
            i.updateBox()

    def movveAll(self):
        for i in self.objectmap.values():
            if i.velocity!=0:
                i.moove()
        return
    
    def checkColli(self,obj):
        toCollide=[]
        for i in obj.boxPosPrec:
            c=self.container[i[1]][i[0]]
            for j in c:
                if j != id(obj) and j not in toCollide:
                    toCollide.append(j)

        return toCollide

def dess(grille):
    for y in range(TAILLEY):
        for x in range(TAILLEX):
            if grille[y][x] == 1:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x * N, y * N, N - 1, N - 1))
            else:
                pygame.draw.rect(screen, pygame.Color(255, 255, 255, 128), pygame.Rect(x * N, y * N, N - 1, N - 1))
    return 

Objects=objects()
c=circle(20,390,10,Objects)
#c1=circle(500,390,10)
Objects.addObject(c)
#Objects.addObject(c1)
c.update(velocity=30,Vdirector=(1/np.sqrt(1**2+1**2),1/np.sqrt(1**2+1**2)))
#c1.update(velocity=40,Vdirector=(-1/np.sqrt(1**2+1**2),1/np.sqrt(1**2+1**2)))

while running:
    screen.fill((115, 117, 117))
    #dess(grille)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        #if event.type == pygame.KEYDOWN:
        #    if event.key==pygame.K_UP:
        #        c.update(0,-N,0)
    Objects.movveAll()
    Objects.updateallBox()
    Objects.paintall()
    
    #for i in Objects.traceList:
    #    pygame.draw.circle(screen, (0, 0, 255), (int(i[0]), int(i[1])), 2)
    pygame.display.update()
    clock.tick(FPS)
quit()