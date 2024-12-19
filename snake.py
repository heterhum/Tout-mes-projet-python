import pygame
import random as rd

STEP=30
X=Y=20
taille_depart=30
pommes=2

screen = pygame.display.set_mode((X*STEP, Y*STEP))
running=True

class snake():
    """
    move act : 1 = UP, 2 = DOWN, 3 =LEFT, 4 = RIGHT
    """
    def __init__(self,longueur,pommes):
        self.mape=[[0 for x in range(X)] for y in range(Y)]
        self.move=[(1,0),(0,1),(0,-1),(-1,0)]
        self.mape[int(Y/2)][int(X/2)]=1
        self.mov_act=3
        self.longueur=longueur
        self.keu=[[int(X/2),int(Y/2)]]
        self.pomme=[[rd.randint(0, int(X/2)-1),rd.randint(0, int(Y/2)-1)] for i in range(pommes)]

    def maj(self):
        self.mape[self.keu[0][1]][self.keu[0][0]]=0
        self.mape[self.keu[-1][1]][self.keu[-1][0]]=1
        for i in self.pomme:
            self.mape[i[1]][i[0]]=2

    def obte(self):
        dispo=[]
        for y in range(Y):
            for x in range(X):
                if self.mape[y][x] != (1 or 2):
                    dispo.append([x,y])
        return dispo

    def check(self):
        if self.keu[-1] in self.pomme:
            self.longueur+=1
            self.pomme.remove(self.keu[-1])
            self.pomme.append(rd.choice(self.obte()))
            return True
        elif 0<=self.keu[-1][0]<X and 0<=self.keu[-1][1]<Y and self.keu[-1] not in self.keu[:-1]:
            return True
        else:
            self.mape=None
            return False

    def right(self):
        n=[]
        for i,j in zip(self.keu[-1],self.move[0]):
            n.append(i+j)
        if len(self.keu)-1==self.longueur:
            self.keu.append(n)
            self.keu.pop(0)
        else:
            self.keu.append(n)
        self.move_act=4
        if self.check():
            self.maj()
            return None
        

    def left(self):
        n=[]
        for i,j in zip(self.keu[-1],self.move[3]):
            n.append(i+j)
        if len(self.keu)-1==self.longueur:
            self.keu.append(n)
            self.keu.pop(0)
        else:
            self.keu.append(n)
        self.move_act=3
        if self.check():
            self.maj()
            return None
    
    def up(self):
        n=[]
        for i,j in zip(self.keu[-1],self.move[2]):
            n.append(i+j)
        if len(self.keu)-1==self.longueur:
            self.keu.append(n)
            self.keu.pop(0)
        else:
            self.keu.append(n)
        self.move_act=1
        if self.check():
            self.maj()
            return None
    
    def down(self):
        n=[]
        for i,j in zip(self.keu[-1],self.move[1]):
            n.append(i+j)
        if len(self.keu)-1==self.longueur:
            self.keu.append(n)
            self.keu.pop(0)
        else:
            self.keu.append(n)
        self.move_act=2
        if self.check():
            self.maj()
            return None
        
    def moove(self):
        match self.mov_act:
            case 1: self.up()
            case 2: self.down()
            case 3: self.left()
            case 4: self.right()

snakee=snake(taille_depart,pommes)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            c=event.key
            if c==pygame.K_UP and snakee.mov_act!=2: snakee.mov_act=1 
            elif c==pygame.K_DOWN and snakee.mov_act!=1: snakee.mov_act=2
            elif c==pygame.K_LEFT and snakee.mov_act!=4: snakee.mov_act=3 
            elif c==pygame.K_RIGHT and snakee.mov_act!=3: snakee.mov_act=4
    pygame.time.wait(250)
    snakee.moove()
    if snakee.mape!=None:
        for y in range(Y):
            for x in range(X):
                if snakee.mape[y][x]==1:
                    pygame.draw.rect(screen,(92, 179, 56),pygame.Rect(x*STEP, y*STEP, STEP, STEP))
                    #pygame.draw.rect(screen,(0,0,0),pygame.Rect(x*STEP, y*STEP, STEP, STEP),width=1,)
                elif snakee.mape[y][x]==2:
                    pygame.draw.rect(screen,(251, 65, 65),pygame.Rect(x*STEP, y*STEP, STEP, STEP))
                    #pygame.draw.rect(screen,(0,0,0),pygame.Rect(x*STEP, y*STEP, STEP, STEP),width=1,)
                else:
                    pygame.draw.rect(screen,(255,255,255),pygame.Rect(x*STEP, y*STEP, STEP, STEP))
                    #pygame.draw.rect(screen,(0,0,0),pygame.Rect(x*STEP, y*STEP, STEP, STEP),width=1,)
    else :
        running=False
    pygame.display.update()
quit()