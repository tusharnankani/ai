import random

def crossover(l, q):
    l = list(l)
    q = list(q)

    k = random.randint(0, len(s)-1)
    print("Crossover point :", k)

    for i in range(k, len(s)):
        l[i], q[i] = q[i], l[i]
    l = ''.join(l)
    q = ''.join(q)
    print(l)
    print(q, "\n")
    return l, q

s = '1100110110110011'
p = '1000110011011111'
print("Parents")
print("P1 :", s)
print("P2 :", p, "\n")

for i in range(5):
    print("Generation", i+1, "Childrens :")
    s, p = crossover(s, p)
