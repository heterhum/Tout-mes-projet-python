import random
import time

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mdp_teste = []
mdp = "azew"
mdp_found = False
essaie = 0
test = None
start_time = time.time()

while essaie <= 1000000:
    trye = random.sample(alphabet, 4)
    test = "".join(trye)
    if test not in mdp_teste :
        mdp_teste.append(test)
        essaie+=1
        if test == mdp:
            print(f"found in {essaie} essaie! it's {test}")
            mdp_found = True
            taketime = time.time() - start_time
            print(f"and it's take : {taketime:.2f}sec")
            break

if mdp_found != True:
    print("raté")