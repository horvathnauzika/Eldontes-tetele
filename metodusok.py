from Szamitogep import Szamitogep

def peldanyositas():
    peldany1 = Szamitogep("win", 32)
    peldany2 = Szamitogep("mac", 16)
    peldany3 = Szamitogep("win", 16)
    szamitogepek = []
    szamitogepek.append(peldany1)
    szamitogepek.append(peldany2)
    szamitogepek.append(peldany3)
    return szamitogepek


def lista_kiiras(lista):
    for i in range(len(lista)):
        oprsz = lista[i].oprsz
        ram = lista[i].ram
        print(f"{oprsz} ({ram})")

# rövid verzió
# lista_kiiras(peldanyositas())

# hosszú verzió
# gepek_listaja = peldanyositas()


def osszegzes_tetele(szamitogepek):
    print("Átlag: ", end="")  # átlag számolás
    gyujto = 0
    for i in range(len(szamitogepek)):
        gyujto += szamitogepek[i].ram
    print(round(gyujto / len(szamitogepek), 3))


def max_tetel(szamitogepek):
    print("Legtöbb ramot tartalmazó oprendszer: ", end="") # max tétel
    max_index = 0
    for i in range(len(szamitogepek)):
        if szamitogepek[i].ram > szamitogepek[max_index].ram:
            max_index = i
    print(szamitogepek[max_index].oprsz)


def megszamlalas_tetel(szamitogepek):
    print("Hány windowsos gépünk van?", end=" ")  # megszámlálás tétel
    db = 0
    for i in range(len(szamitogepek)):
        if szamitogepek[i].oprsz == "win":
            db += 1
    print(f"{db} db windowsos gépünk van")


def eldontes_tetele(szamitogepek):
    vizsgalt_ram = 16
    print(f"Van e {vizsgalt_ram} gbnél nagyobb windows?", end=" ")  # eldöntés tétele
    valtozo = False
    for i in range(len(szamitogepek)):
        if "win" in szamitogepek[i].oprsz and szamitogepek[i].ram > vizsgalt_ram:
            valtozo = True
    if valtozo == True:
        print("Igen, van")
    else:
        print("Nem, nincs")


gepek_listaja = peldanyositas()
lista_kiiras(gepek_listaja)
osszegzes_tetele(gepek_listaja)
max_tetel(gepek_listaja)
megszamlalas_tetel(gepek_listaja)
eldontes_tetele(gepek_listaja)