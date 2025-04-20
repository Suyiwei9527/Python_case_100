#test self
import random
l = []
for i in range (10):
    l.append(random.randint(1,5000))
def bubble(l):
    for i in range (len(l) - 1):
        for j in range (len(l) - i - 1):
            if l [j] > l [j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    return l
print(bubble(l))