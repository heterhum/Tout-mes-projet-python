import pygame
import numpy as np
import scipy as sp

TAILLEX=800
TAILLEY=800
screen = pygame.display.set_mode((TAILLEX,TAILLEY))

FPSM=120
FPSA=60
pygame.init()
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

        self.EarthMass=5.9722e24
        self.MoonMass=7.34767309e22

        self.color=(255,255,255)
        self.radius=2

    def Gravitation(self,d,m1,m2): #meter and Kg
        f=sp.constants.G * (m1*m2)/d**2
        return f

    def updateVector(self,target):
        dire = target * self.PixToMe - self.Rxy
        dire = normalise(dire) #vector toward Earth

        distance=np.linalg.vector_norm(target*self.PixToMe-self.Rxy) #meter
        t1=self.Gravitation(distance,self.EarthMass,self.MoonMass) #Newton
        t1=t1/self.MoonMass
        Force=dire*t1*(21600) #delta P = F * delta t -> P2=F*delta+P1 = Vector towards earth ; 21600 sec is 1 month every sec irl
        new=Force+self.Vmouvement 
        v=np.linalg.norm(new) #speed

        return v,new
    
    def move(self,mx,my): 
        v,vec=self.updateVector(np.array([mx,my]))

        self.v=v
        self.Vmouvement=vec

        self.Rxy=np.add(self.Rxy,vec) #why, how it's working, idk, it's not physic it's fisique
        self.xy=self.Rxy/self.PixToMe
        return

    def TradXY(self):
        return int(self.xy[0].item()),int(self.xy[1].item())

    def draw(self,screen):
        xy=self.TradXY()
        print(xy)
        pygame.draw.circle(screen,self.color,xy,self.radius)
        #pygame.draw.line(screen,(255,0,0),(int(self.x),int(self.y)),(int(self.x+self.vector[0]),int(self.y+self.vector[1])),2)
        return

running = True
clock=pygame.time.Clock()
runner=SolarSys()
EarthPos=[TAILLEX//2,TAILLEY//2]

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #pos = pygame.mouse.get_pos()
    #runner.move(pos[0], pos[1],1)
    runner.move(EarthPos[0],EarthPos[1])
    runner.draw(screen)

    pygame.draw.circle(screen,(0,255,0),(EarthPos[0],EarthPos[1]),13)
    pygame.display.update()
    clock.tick(FPSM)