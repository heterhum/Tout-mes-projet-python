from pygame import *
TAILLEX,TAILLEY,N,MOVE = 50,50,20,[(1, 1), (0, 1), (-1, 1),(1, -1), (0, -1), (-1, -1),(1, 0), (-1, 0)]
grille_num,screen = [[0 for j in range(TAILLEX)] for i in range(TAILLEY)],display.set_mode((N * TAILLEX, N * TAILLEY))
pause=running = True
def check(grille, x, y):
    s = 0
    for i in MOVE:
        x1, y1 = i
        if 0 <= x + x1 < TAILLEX and 0 <= y + y1 < TAILLEY:
            if grille[y + y1][x + x1] == 1: s += 1
    if s == 3: return 1
    elif s == 2: return grille[y][x]
    else: return 0
def dess(grille):
    for y in range(TAILLEY):
        for x in range(TAILLEX):
            if grille[y][x] == 1:
                draw.rect(screen, (0, 0, 0), Rect(x * N, y * N, N - 1, N - 1))
            else:
                draw.rect(screen, (255, 255, 255), Rect(x * N, y * N, N - 1, N - 1))
while running:
    dess(grille_num)
    for evente in event.get():
        if evente.type == QUIT: running = False
        if evente.type == MOUSEBUTTONDOWN:
            pos = mouse.get_pos()
            grille_num[pos[1] // N][pos[0] // N] = 1
        if evente.type == KEYDOWN and evente.key==K_p: pause=not pause
    if not pause:
        grilles=[i.copy() for i in grille_num]
        for y in range(TAILLEY):
            for x in range(TAILLEX):
                grille_num[y][x] = check(grilles, x, y)
        time.wait(500)
    display.update()
quit()