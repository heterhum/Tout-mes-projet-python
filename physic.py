import pygame
import random as rd
import numpy as np

# 10 pixels = 1m
pixel_to_m=10
WIDTH, HEIGHT = 600, 400
N=50
TAILLEX = WIDTH // N
TAILLEY = HEIGHT // N

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
        return



class circle():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self._velocity=0 # m/s
        self._masse=1 # kg
        self.rebond=100
        self._Ecin=(1/2)*self.masse*self.velocity**2
        self.Vdirector=(1,0)
        self.objectsclass=objects()
        self.physic=Physic()

    def update_Ecin(self):
        self._Ecin = 0.5 * self._masse * (self._velocity ** 2)
        return

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
        pygame.draw.line(screen, (255,0,0), (self.x,self.y), (self.x+(self.Ecin*self.Vdirector[0]),self.y-(self.Ecin*self.Vdirector[1])), width=2)

    def update(self,x=None,y=None,r=None,velocity=None,rebond=None,masse=None,Vdirector=None):
        if x is not None:
            self.x=x
        if y is not None:
            self.y=y
        if r is not None:
            self.r=r
        if velocity is not None:
            self.velocity=velocity  
        if rebond is not None:
            self.rebond=rebond
        if masse is not None:
            self.masse=masse
        if Vdirector is not None:
            self.Vdirector=Vdirector
        return 

    def getParam(self):
        return (self.x, self.y,self.r)
    
    def updateBox(self):
        rightTo=int((self.x+self.r)//N)
        leftTo=int((self.x-self.r)//N)
        topTo=int((self.y-self.r)//N)
        botTo=int((self.y+self.r)//N)
        
        lSend=[]
        for y in range(topTo,botTo+1):
            for x in range(leftTo,rightTo+1):
                check=self.objectsclass.addContainer(self,x,y)
                if check:
                    grille[y][x]=1
                    lSend.append((x,y))
        self.objectsclass.updateContainer(self,lSend)
        return
    
    def moove(self):
        newxy=self.physic.gravVcalc(self)
        x=newxy[0]
        y=newxy[1]
        self._velocity=newxy[2]
        self.Vdirector=newxy[3]
        if 0<=x+self.r<=WIDTH and 0<=y+self.r<=HEIGHT and 0<=x-self.r<=WIDTH and 0<=y-self.r<=HEIGHT:
            self.x=x
            self.y=y
        else:
            self.update(velocity=0,Vdirector=(0,0))
        return


class objects():
    def __init__(self):
        self.objectmap={}
        self.container=[[[] for x in range(TAILLEX)] for y in range(TAILLEY)]
        self.traceList=[]

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
    
    def delContainer(self,obj,x,y):
        self.container[y][x].remove(id(obj))
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

    def updateContainer(self,obj,Lcheck):
        ide=id(obj)
        for y in range(TAILLEY):
            for x in range(TAILLEX):
                if ide in self.container[y][x] and (x,y) not in Lcheck:
                    self.delContainer(obj,x,y)
                    grille[y][x]=0

def dess(grille):
    for y in range(TAILLEY):
        for x in range(TAILLEX):
            if grille[y][x] == 1:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x * N, y * N, N - 1, N - 1))
            else:
                pygame.draw.rect(screen, pygame.Color(255, 255, 255, 128), pygame.Rect(x * N, y * N, N - 1, N - 1))
    return 

Objects=objects()
c=circle(20,380,20)
Objects.addObject(c)
c.update(velocity=30,Vdirector=(1/np.sqrt(1+0.8**2),0.8/np.sqrt(1+0.8**2)))

while running:
    screen.fill((115, 117, 117))
    #dess(grille)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                c.update(0,-N,0)
    c.moove()
    Objects.paintall()
    Objects.updateallBox()
    #for i in Objects.traceList:
    #    pygame.draw.circle(screen, (0, 0, 255), (int(i[0]), int(i[1])), 2)
    pygame.display.update()
    clock.tick(FPS)
quit()