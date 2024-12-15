import pygame
TAILLEX = 50
TAILLEY = 50
N = 20
MOVE = [(1, 1), (0, 1), (-1, 1),(1, -1), (0, -1), (-1, -1),(1, 0), (-1, 0)]
grille_num = [[0 for j in range(TAILLEX)] for i in range(TAILLEY)]
screen = pygame.display.set_mode((N * TAILLEX, N * TAILLEY))
fist_grille = True
pause=True
running = True
def check(grille, x, y):
    s = 0
    for i in MOVE:
        x1, y1 = i
        if 0 <= x + x1 < TAILLEX and 0 <= y + y1 < TAILLEY:
            if grille[y + y1][x + x1] == 1:
                s += 1
    if s == 3:
        return 1
    elif s == 2:
        return grille[y][x]
    else:
        return 0
def dess(grille):
    for y in range(TAILLEY):
        for x in range(TAILLEX):
            if grille[y][x] == 1:
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x * N, y * N, N - 1, N - 1))
            else:
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x * N, y * N, N - 1, N - 1))
while running:
    dess(grille_num)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            grille_num[pos[1] // N][pos[0] // N] = 1
        if event.type == pygame.KEYDOWN and event.key==pygame.K_p: pause=not pause
    if not pause:
        grilles=[i.copy() for i in grille_num]
        for y in range(TAILLEY):
            for x in range(TAILLEX):
                grille_num[y][x] = check(grilles, x, y)
        pygame.time.wait(500)
    pygame.display.update()
quit()