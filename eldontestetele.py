import math
def tetel():
    n = int(input("\nszám: "))
    prim = True
    if n < 2:
        prim = False
    else:
        i = 2
        while(i <= math.sqrt(n) and n % i != 0):
            i = i + 1
        prim = i > math.sqrt(n)
    if prim:
        print("Prím")
    else:
        print("Nem prím")