from Szamitogep import Szamitogep


peldany1 = Szamitogep("win", 32)
peldany2 = Szamitogep("mac", 16)
peldany3 = Szamitogep("win", 16)
szamitogepek = []
szamitogepek.append(peldany1)
szamitogepek.append(peldany2)
szamitogepek.append(peldany3)
for i in range(len(szamitogepek)):
    oprsz = szamitogepek[i].oprsz
    ram = szamitogepek[i].ram
    print(f"{oprsz} ({ram})")

print("Átlag: ", end="") # átlag számolás, összegzés tétel
gyujto = 0
for i in range(len(szamitogepek)):
    gyujto += szamitogepek[i].ram
print(round(gyujto/len(szamitogepek), 3))

print("Legtöbb ramot tartalmazó oprendszer: ", end="") # max tétel
max_index = 0
for i in range(len(szamitogepek)):
    if szamitogepek[i].ram > szamitogepek[max_index].ram:
        max_index = i
print(szamitogepek[max_index].oprsz)

print("Hány windowsos gépünk van?", end=" ") # megszámlálás tétel
db = 0
for i in range(len(szamitogepek)):
    if szamitogepek[i].oprsz == "win":
        db += 1
print(f"{db} db windowsos gépünk van")

vizsgalt_ram = 16
print(f"Van e {vizsgalt_ram} gbnél nagyobb windows?", end=" ") # eldöntés tétele
valtozo = False
for i in range(len(szamitogepek)):
    if "win" in szamitogepek[i].oprsz and szamitogepek[i].ram > vizsgalt_ram:
        valtozo = True
if valtozo  == True:
    print("Igen, van")
else:
    print("Nem, nincs")
