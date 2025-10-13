import pygame
import random as rd
import numpy as np
import time
#ceci m'a couté un week-end de ma vie
#ne pas mettre des vitesse trop abérrante, c'est possible que je ne comprenne pas le bug généré
#TO DO : ajouter du random

PIXELTOMETER=10 #10 pixels = 1m
WIDTH, HEIGHT = 1000, 600
N=50
TAILLEX, TAILLEY= (WIDTH // N)+1, (HEIGHT // N)+1
FPS = 120

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True

class Physic():
    def __init__(self):
        self.gravity=9.81 # m/s^2 9.81

    def Vcalc(self,v,vector,x,y): #calcule nouvelle position
        distance=v*(1/FPS)
        Pdistance=(distance*PIXELTOMETER)
        Vx=Pdistance*vector[0]
        Vy=Pdistance*vector[1]
        x+=Vx
        y-=Vy

        return x,y
    
    def gravVcalc(self,v,vector,x,y):
        Nvector=(vector[0]*v,vector[1]*v+(1/FPS)*(-self.gravity)) #calcule nouveau vecteur directeur avec la gravité
        norme=self.norme(Nvector)
        NewVector=self.Vnormale(Nvector,norme)
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
        NewV=(obj1.Vdirector[0]-tosou[0],obj1.Vdirector[1]-tosou[1]) #vecteur directeur aprés boing

        norme=self.norme(NewV)
        NewV=self.Vnormale(NewV,norme)

        obj1.update(velocity=obj1.coefResti*obj1.velocity,Vdirector=NewV)
    
        return True
    
class Objects():
    def __init__(self):
        self.objectmap={} #liste des objets présents
        self.container=[[[] for x in range(TAILLEX)] for y in range(TAILLEY)] #liste des objet dans chaque boite
        
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

    def addObject(self,obj): #traduit
        self.objectmap[id(obj)]=obj
        return id(obj)
    
    def removeObject(self,obj): #traduit (encore)
        del self.objectmap[id(obj)]
        return id(obj)
    
    def addContainer(self,obj,x,y): #ajoute l'id de l'objet présent dans la boite x,y
        if 0<=x<TAILLEX and 0<=y<TAILLEY and id(obj) not in self.container[y][x]:
            self.container[y][x].append(id(obj))
            return True
        return False
    
    def delContainer(self,objid,x,y):
        self.container[y][x].remove(objid)
        return

    def paintall(self):
        for i in self.objectmap.values():
            i.draw()
            i.drawVector()
        return
    
    def updateallBox(self):
        for i in self.objectmap.values():
            i.UpdateBox() #chaque objet gere ou il ce trouve dans la grille

    def movveAll(self):
        for i in self.objectmap.values():
            if i.Vdirector!=(0,0) and i.velocity!=0: #on évite de faire bouger les objets immobiles
                i.moove()
        return
    
    def checkColli(self,obj): #on regarde les potentiels colision
        toCollide=[]
        for i in obj.boxPosPrec:
            c=self.container[i[1]][i[0]]
            for j in c:
                if j != id(obj) and j not in toCollide:
                    toCollide.append(j)
        return toCollide
    
class circle():
    def __init__(self, x, y, r,objets,physic):
        self.x = x
        self.y = y
        self.r = r # pixel
        self._velocity=0 # m/s
        self._masse=1 # kg
        self.coefResti=0.83 #0.83
        self._Ecin=0
        self.Vdirector=(1,0)
        self.boxPosPrec=[]
        self.WallCooldown=0.1 # case occupée actuellement ou avant ( sa dépend a quelle moment on ce situe )

        self.Objects=objets
        self.Physic=physic
        
        self.UpdateEcin()
        self.UpdateBox()
        self.cooldown=time.time()

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
        self.UpdateEcin()
        return
    @masse.setter
    def masse(self,m):
        self._masse=m
        self.UpdateEcin()
        return

    def UpdateEcin(self):
        self._Ecin = 0.5 * self._masse * (self._velocity ** 2)
        return

    def cooldownstart(self):
        self.cooldown=time.time()
        return
    
    def cooldowncheck(self):
        if time.time()-self.cooldown>=self.WallCooldown:
            return True
        return False

    def draw(self):
        pygame.draw.circle(screen, (138, 16, 3), (self.x, self.y), self.r)
        return
    def drawVector(self): 
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

    def UpdateBox(self): #donne toute les cases occupées par le cercle
        rightTo=int((self.x+self.r)//N)
        leftTo=int((self.x-self.r)//N)
        topTo=int((self.y-self.r)//N)
        botTo=int((self.y+self.r)//N)

        CaseOccupe=[]
        for y in range(topTo,botTo+1):
            for x in range(leftTo,rightTo+1):
                if 0<=x<TAILLEX and 0<=y<TAILLEY:
                    CaseOccupe.append((x,y))
                    self.Objects.addContainer(self,x,y) #l'ajoute a la grille de boite

        if self.boxPosPrec != []:
                for i in self.boxPosPrec:
                    if i not in CaseOccupe:
                        self.Objects.delContainer(id(self),i[0],i[1])
                        
        self.boxPosPrec=CaseOccupe
        return 
    
    def tuchWall(self,x,y): #x,y nouvelle position si pas de mur
        if not (0<=self.x+self.r<=WIDTH and 0<=self.y+self.r<=HEIGHT and 0<=self.x-self.r<=WIDTH and 0<=self.y-self.r<=HEIGHT) : #touche un mur quelquonque ?
            if self.x+self.r>WIDTH: #trouve quelle coté
                obj=mur("droite")
                self.x=WIDTH-self.r
            if self.x-self.r<0:
                obj=mur("gauche")
                self.x=self.r
            if self.y+self.r>HEIGHT:
                obj=mur("bas")
                self.y=HEIGHT-self.r
            if self.y-self.r<0:
                obj=mur("haut")
                self.y=self.r

            if self.cooldowncheck():
                self.Physic.Collimur(self,obj) #modifie direct vitesse et vecteur
                newxy=self.Physic.gravVcalc(self.velocity,self.Vdirector,self.x,self.y)
                self.update(x=newxy[0],y=newxy[1])
                self.cooldownstart() #reset coolodown
                print("boing")
            if self.velocity<0.7 and self.y>=HEIGHT-self.r-1:
                print("stuck")
                self.velocity=0
                self.Vdirector=(0,0)
                self.y=HEIGHT-self.r
        else:
            self.x=x
            self.y=y
        return

    def moove(self):
        u=self.Objects.checkColli(self) #liste des objets a tester
        newxy=self.Physic.gravVcalc(self.velocity,self.Vdirector,self.x,self.y)
        x=newxy[0]
        y=newxy[1]
        self.update(velocity=newxy[2],Vdirector=newxy[3])

        modif=False
        if u != []:
            for i in u:
                uh=self.Objects.objectmap[i]
                match uh:
                    case mur():
                        self.tuchWall(x,y) #mais direct a jour
                        modif=True
                    case circle():
                        pass
        if not modif:
            self.x=x
            self.y=y
        return

class mur():
    def __init__(self, d):
        self.d = d
        self.vnorm=self.getVector()
        self.velocity=0
        self.Vdirector=(0,0)
        
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
    def UpdateBox(self):
        return

objects=Objects()
physic=Physic()

c=circle(20,390,10,objects,physic)
c1=circle(500,390,10,objects,physic)
objects.addObject(c)
objects.addObject(c1)
c.update(velocity=40,Vdirector=physic.Vnormale((1,1),physic.norme((1,1))))
c1.update(velocity=40,Vdirector=physic.Vnormale((1,1),physic.norme((1,1))))


while running:
    screen.fill((115, 117, 117))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    objects.movveAll()
    objects.updateallBox()
    objects.paintall()

    pygame.display.update()
    clock.tick(FPS)
quit()