import pygame
TAILLEX = 9
TAILLEY = 9
N = 50

grille_num = [[0 for j in range(TAILLEX)] for i in range(TAILLEY)]
screen = pygame.display.set_mode((N * TAILLEX, N * TAILLEY))
pause=True
running = True

def dess(grille):
    for y in range(TAILLEY):
        for x in range(TAILLEX):
            if grille[y][x] == 1:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x * N, y * N, N - 1, N - 1))
            else:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x * N, y * N, N - 1, N - 1))

def incircle(x,y,r,xm,ym):
    x,y=x+1,y+1
    if (xm-x)**2+(3-y)**2-r**2==0:
        return True
    elif (ym-x)**2+(3-y)**2<r**2:
        return True
    else:
        return False

def circle(grille,x,y,r):
    y1=y-r
    lim=x+r
    xm=x
    ym=y
    while x<lim:
        if incircle(x,y1+0.5,r,xm,ym):
            grille[y1][x]=1
        else:
            grille[y1+1][x]=1
            grille[y1+1][x-1]=1
            y1+=1
        x+=1
        print(x,y1)
    iso=[]
    yu=0
    for y in range(ym-r,ym-r+2):
        iso.append([])
        
        for x in range(xm,xm+r+1):
            iso[yu].append(grille[y][x])
        yu+=1
    print(iso)
    return iso

circle(grille_num,4,4,3)

while running:
    dess(grille_num)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            grille_num[pos[1] // N][pos[0] // N] = 1
    
    pygame.time.wait(100)
    pygame.display.update()
quit()