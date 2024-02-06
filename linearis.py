def linearis(also, felso):
    i = also
    while( i <= felso and (i % 10 != 0)):
        i += 1
    van = i <= felso
    if van:
        return "Van 0-ra végződő szám"
    else:
        return "Nincs 0-ra végződő szám"

print(linearis(42, 67))