import pygame

pygame.init()
N=20
STEP=20
WIDTH=N*STEP
HEIGHT=N*STEP
running=True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

move=[(1,0),(0,1),(0,-1),(-1,0)]

class pacman():
    def __init__(self):
        self.mape=[[0 for x in range(N)] for y in range(N)]
        self.position=[int(N/2),int(N/2)]
        self.mape[self.position[1]][self.position[0]]=1
        self.move=[(1,0),(0,1),(0,-1),(-1,0)]
        self.mooveactuel="up"

    def up(self):
        self.mooveactuel="up"
        if self.position[1]==0:
            self.mape[self.position[1]][self.position[0]]=0
            self.position[1]=N-1
        else:
            self.mape[self.position[1]][self.position[0]]=0
            self.position[1]-=1
            self.mape[self.position[1]][self.position[0]]=1

    def down(self):
        self.mooveactuel="down"
        if self.position[1]==N-1:
            self.mape[self.position[1]][self.position[0]]=0
            self.position[1]=0
        else:
            self.mape[self.position[1]][self.position[0]]=0
            self.position[1]+=1
            self.mape[self.position[1]][self.position[0]]=1

    def right(self):
        self.mooveactuel="right"
        if self.position[0]==N-1:
            self.mape[self.position[1]][self.position[0]]=0
            self.position[0]=0
        else:
            self.mape[self.position[1]][self.position[0]]=0
            self.position[0]+=1
            self.mape[self.position[1]][self.position[0]]=1

    def left(self):
        self.mooveactuel="left"
        if self.position[0]==0:
            self.mape[self.position[1]][self.position[0]]=0
            self.position[0]=N-1
        else:
            self.mape[self.position[1]][self.position[0]]=0
            self.position[0]-=1
            self.mape[self.position[1]][self.position[0]]=1







pacman=pacman()
while running:
    screen.fill((255, 255, 255))
    keydown=True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP: pacman.up()
                case pygame.K_DOWN: pacman.down()
                case pygame.K_RIGHT: pacman.right()
                case pygame.K_LEFT: pacman.left()
            keydown=True
        elif event.type == pygame.KEYUP:
            keydown=False

    if keydown==False:
        match pacman.mooveactuel:
            case "up": pacman.up()
            case "down": pacman.down()
            case "right": pacman.right()
            case "left": pacman.left()
    
    for y in range(N):
        for x in range(N):
            if pacman.mape[y][x]==1:
                pygame.draw.rect(screen,(0,0,0),pygame.Rect(x*STEP, y*STEP, STEP, STEP))
            pygame.draw.rect(screen,(0,0,0),pygame.Rect(x*STEP, y*STEP, STEP, STEP),width=1)
    
    clock.tick(5)
    pygame.display.update()
quit()