mdp = "anatole"

myfile = open("C:/Users/xoxar/Downloads/listemdp.txt", "r")

while True:
    line  = myfile.readline()
    if line.strip() == mdp:
        print(line)
        break
myfile.close() 