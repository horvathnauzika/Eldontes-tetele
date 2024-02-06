import math

def kivalasztas_tetele():
    prim = False
    n = 9999
    while(prim == False):
        n += 1
        i = 2
        while  (i <= math.sqrt(n) and n % i != 0):
            i += 1
        prim = i > math.sqrt(n)
    return n

print(kivalasztas_tetele())

