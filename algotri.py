import random
x1=[2,6,8,4,1,11]
y=[]
#x1 = list(range(1, 1001))
#random.shuffle(x1)


count=0
for i in range(1,len(x1)):
    for e in x1:
        if x1[i]<e:
            x1.insert(x1.index(e),x1.pop(i))
            count+=1

for _ in range(len(x1)):
    e=x1[0]
    for i in range(len(x1)):
        if x1[i]>e:
            e=x1[i]
    y.append(e)
    x1.remove(e)

for t in range(len(x1)):
    e=x1[0]
    for i in range(len(x1)-t):
        if x1[i]>e:
            e=x1[i]
    x1.append(e)
    x1.remove(e)


