import pygame
import random

class base:
    def __init__(self):
        self.TAILLEX = 50
        self.TAILLEY = 50
        self.N = 20
        self.MOVE = [(1, 1), (0, 1), (-1, 1),(1, -1), (0, -1), (-1, -1),(1, 0), (-1, 0)]
        self.grille_num = [[0 for j in range(self.TAILLEX)] for i in range(self.TAILLEY)]
        self.screen = pygame.display.set_mode((self.N * self.TAILLEX, self.N * self.TAILLEY))
        self.fist_grille = True
        self.pause=True
        self.running = True
        self.random_pourcent=40
        self.velocite=100
        
        self.BrushDown=False
        self.BrushActSquare=None
        

    def dessjdlv(self):
        for y in range(self.TAILLEY):
            for x in range(self.TAILLEX):
                if self.grille_num [y][x] == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(x * self.N, y * self.N, self.N - 1, self.N - 1))
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x * self.N, y * self.N, self.N - 1, self.N - 1))

    def prob(self,p):
        c=random.randint(0,100)
        if c<p:
            return 1
        return 0
    
class JDLV(base):
    def __init__(self):
        super().__init__()

    def check(self,grille, x, y):
        s = 0
        for i in self.MOVE:
            x1, y1 = i
            if 0 <= x + x1 < self.TAILLEX and 0 <= y + y1 < self.TAILLEY:
                if grille[y + y1][x + x1] == 1:
                    s += 1
        if s == 3 or s==6:
            return 1
        elif s == 2 or s==3:
            return grille[y][x]
        else:
            return 0
        
    def randomize(self,p):
        for y in range(self.TAILLEY):
            for x in range(self.TAILLEX):
                self.grille_num[y][x]=self.prob(p)
        return 
        
    def grille_modif(self):
        grilles=[i.copy() for i in self.grille_num]
        for y in range(self.TAILLEY):
            for x in range(self.TAILLEX):
                self.grille_num[y][x] = self.check(grilles, x, y)
        return

    def JDLV_eventHandler(self):
        
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:  
                    self.running = False
                case pygame.MOUSEBUTTONDOWN:
                    self.BrushDown=True
                    pos = pygame.mouse.get_pos()
                    self.BrushActSquare=(pos[0] // self.N,pos[1] // self.N)
                    self.grille_num[pos[1] // self.N][pos[0] // self.N] = not self.grille_num[pos[1] // self.N][pos[0] // self.N]
                case pygame.MOUSEBUTTONUP:
                    self.BrushDown=False
                case pygame.MOUSEMOTION if self.BrushDown and self.pause:
                    pos = pygame.mouse.get_pos()
                    squarepos = (pos[0] // self.N,pos[1] // self.N)
                    if 0 <= squarepos[0] < self.TAILLEX and 0 <= squarepos[1] < self.TAILLEY:
                        if self.BrushActSquare!=squarepos:
                            self.BrushActSquare=squarepos
                            self.grille_num[squarepos[1]][squarepos[0]] = not self.grille_num[squarepos[1]][squarepos[0]]
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_p:
                            self.pause=not self.pause
                        case pygame.K_r if self.pause:
                            self.randomize(self.random_pourcent)
                        case pygame.K_u if self.pause:
                            self.grille_num = [[0 for j in range(self.TAILLEX)] for i in range(self.TAILLEY)]

    def BJDLV(self):
        while self.running:
            self.dessjdlv()
            self.JDLV_eventHandler()
            if not self.pause:
                self.grille_modif()
                pygame.time.wait(self.velocite)
            pygame.display.update()
        quit()
    

if __name__ == "__main__":
    jeu=JDLV()
    jeu.BJDLV()