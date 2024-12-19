import pygame

N=10
STEP=70

screen = pygame.display.set_mode((N*STEP, N*STEP))
running=True


class snake():
    """
    move act : 1 = UP, 2 = DOWN, 3 =LEFT, 4 = RIGHT
    """
    def __init__(self):
        self.mape=[[0 for x in range(N)] for y in range(N)]
        self.move=[(1,0),(0,1),(0,-1),(-1,0)]
        self.mape[5][5]=1
        self.mov_act=3
        self.longueur=4
        self.keu=[[1,5],[2,5],[3,5],[4,5],[5,5]]

    def maj(self):
        self.mape[self.keu[0][1]][self.keu[0][0]]=0
        self.mape[self.keu[-1][1]][self.keu[-1][0]]=1
        #for i in self.keu:
        #    self.mape[i[-1]][i[0]]=1

    def check(self):
        if 0<=self.keu[-1][0]<N and 0<=self.keu[-1][1]<N:
            return True
        else:
            self.mape=None
            return False

    def right(self):
        n=[]
        for i,j in zip(self.keu[-1],self.move[0]):
            n.append(i+j)
        print(n)
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

snakee=snake()
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
        for y in range(N):
            for x in range(N):
                if snakee.mape[y][x]==1:
                    pygame.draw.rect(screen,(255,0,255),pygame.Rect(x*STEP, y*STEP, STEP, STEP))
                    pygame.draw.rect(screen,(0,0,0),pygame.Rect(x*STEP, y*STEP, STEP, STEP),width=1,)
                else:
                    pygame.draw.rect(screen,(255,255,255),pygame.Rect(x*STEP, y*STEP, STEP, STEP))
                    pygame.draw.rect(screen,(0,0,0),pygame.Rect(x*STEP, y*STEP, STEP, STEP),width=1,)
    else :
        running=False
    pygame.display.update()
    
    
    
    
    
        #def move(m,tabl):
    #    table=tabl.copy()
    #    new=[]
    #    table[keu[-1][1]][keu[-1][0]]=0
    #    if m==1 and mov_act!=2: #down
    #        #emplacement=(emplacement[0]-1,emplacement[1])
    #        for i,j in zip(keu[-1],MOVE[m]):
    #            new.append(i+j)
    #        keu[-1]=new.copy()
    #        if 0<=keu[-1][0]<=N and 0<=keu[-1][1]<=N:
    #            table[keu[-1][1]][keu[-1][0]]=1
    #            return table
    #        else:
    #            return None
    #    if m==2 and mov_act!=1: #up
    #        #keu[-1]=(keu[-1][0]-1,keu[-1][1])
    #        for i,j in zip(keu[-1],MOVE[m]):
    #            new.append(i+j)
    #        keu[-1]=new.copy()
    #        if 0<=keu[-1][0]<=N and 0<=keu[-1][1]<=N:
    #            table[keu[-1][1]][keu[-1][0]]=1
    #            return table
    #        else:
    #            return None
    #    if m==3 and mov_act!=0: #left
    #        #keu[-1]=(keu[-1][0]-1,keu[-1][1])
    #        for i,j in zip(keu[-1],MOVE[m]):
    #            new.append(i+j)
    #        keu[-1]=new.copy()
    #        if 0<=keu[-1][0]<=N and 0<=keu[-1][1]<=N:
    #            table[keu[-1][1]][keu[-1][0]]=1
    #            return table
    #        else:
    #            return None
    #    if m==0 and mov_act!=3: #right
    #        #keu[-1]=(keu[-1][0]-1,keu[-1][1])
    #        for i,j in zip(keu[-1],MOVE[m]):
    #            new.append(i+j)
    #        keu[-1]=new.copy()
    #        if 0<=keu[-1][0]<=N and 0<=keu[-1][1]<=N:
    #            table[keu[-1][1]][keu[-1][0]]=1
    #            return table
    #        else:
    #            return None
    #    return tabl
