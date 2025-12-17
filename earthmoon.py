import pygame
import numpy as np
import scipy as sp

TAILLEX=800
TAILLEY=800
screen = pygame.display.set_mode((TAILLEX,TAILLEY))

FPSM=120

pygame.init()
myfont = pygame.font.SysFont("monospace", 15)
#1000Km -> 1 pixel
def normalise(vect):
    norm = np.linalg.vector_norm(vect)
    if norm > 1e-8:
        return vect / norm
    return np.zeros_like(vect)

class SolarSys:
    def __init__(self):
        self.v=0
        self.PixTokm=1000
        self.PixToMe=self.PixTokm*10**3
        self.xy=np.array([100,100])
        self.Rxy=np.array([100,100])*self.PixToMe
        self.Vmouvement=np.array([0,0])

        self.EarthMass=5.9722e24 #kg
        self.MoonMass=7.34767309e22 #kg
        self.MoonDistance=3.85e8

        self.color=(255,255,255)
        self.radius=2

        self.HourWanted=24 #number of hour in 1 sec irl

        self.dt=(self.HourWanted*3600)/FPSM #1 sec irl is 120 frame in game, i want 1 sec to be 1 month so 1 month to sec / 120

        
    def initcalc(self):
        v=np.sqrt((sp.constants.G*self.EarthMass)/self.MoonDistance) #init speed m/s
        vec=v*np.array([1,0]) #to right

        EarthPos=np.array([TAILLEX//2,TAILLEY//2])*self.PixToMe

        self.Rxy=EarthPos+np.array([0,-self.MoonDistance])
        
        distance=np.linalg.vector_norm(EarthPos-self.Rxy) #meter
        t1=self.Gravitation(distance,self.EarthMass) #Newton
        new=np.array([0,-1])*t1*self.dt+vec

        self.xy=self.Rxy/self.PixToMe
        self.Vmouvement=new
        return

    def Gravitation(self,d,m1): #meter and Kg
        f=sp.constants.G * m1/d**2
        return f

    def updateVector(self,target):
        target=target*self.PixToMe
        dire = target - self.Rxy
        dire = normalise(dire) #vector toward Earth

        distance=np.linalg.vector_norm(target-self.Rxy) #meter
        Acc=self.Gravitation(distance,self.EarthMass) #Newton
        
        Vacc=dire*Acc*self.dt #delta V = A * delta t -> V2=A*delta+V1 = Vector towards earth ; 21600 sec is 1 month every sec irl
        new=Vacc+self.Vmouvement #V2 = F 
        v=np.linalg.norm(new) 

        return v,new
    
    def move(self,mx,my): 
        v,vec=self.updateVector(np.array([mx,my]))

        self.v=v
        self.Vmouvement=vec

        self.Rxy=np.add(self.Rxy,vec*self.dt) #position + Vspeed*dt -> position
        self.xy=self.Rxy/self.PixToMe #meter to pixel
        return

    def TradXY(self):
        return int(self.xy[0].item()),int(self.xy[1].item()) #to get xy pos in int

    def draw(self,screen):
        xy=self.TradXY()
        pygame.draw.circle(screen,self.color,xy,self.radius) #moon
        pygame.draw.line(screen,(255,0,0),xy,xy+(self.Vmouvement/self.PixToMe),1) #vector
        return

running = True
clock=pygame.time.Clock()

runner=SolarSys()
runner.initcalc()

EarthPos=[TAILLEX//2,TAILLEY//2]

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    runner.move(EarthPos[0],EarthPos[1])
    runner.draw(screen)

    label = myfont.render(str(round(runner.v,2))+" m/s", 1, (255,255,0))
    label1 = myfont.render(str(round(pygame.time.get_ticks()/1000,4)) + " seconde", 1, (255,255,0))
    label2 = myfont.render(str(round((pygame.time.get_ticks()/1000)*runner.HourWanted,4))+ " hour", 1, (255,255,0))
    screen.blit(label, (100, 100))
    screen.blit(label1, (100, 120))
    screen.blit(label2, (100, 140))
    pygame.draw.circle(screen,(0,255,0),(EarthPos[0],EarthPos[1]),13)
    pygame.display.update()
    clock.tick(FPSM)