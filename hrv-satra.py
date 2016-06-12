#prevodilac HRV u ZG-SATRA
#autor: Fran Raknic

samoglasnici = ['a','e','i','o','u']
interpunkcija = ['.',',',':','?','!',';']

#TODO:
#dodati iznimke za rijeci od 3 slova
#prevodilac satra -> HRV
#formatirati ispis lowercase, capitalize etc.
#formatirati input

#razdvajanje rijeci na slogove
def Fslogovi(rijec):
    slogovi = []
    for i in range(0, len(rijec)):
        if rijec[i] in samoglasnici:
            slogovi.append(rijec[:i+1:])
            slogovi.append(rijec[i+1::])
            break
    return slogovi


def testWord(rijec):
    if interpunkcija in rijec:
        return rijec.pop()

#prevodi prima recenicu, vraca prevedeno
def prevodi(tekst):
    tmpPrjevod = []
    prijevod = []
    tekst = tekst.split()

    for rijec in tekst:
        tmpPrjevod.append(Fslogovi(rijec))
    for rijec in tmpPrjevod:
        prijevod.append(" ")
        for slog in reversed(rijec):
            prijevod.append(slog)
    prijevod = "".join(prijevod)
    prijevod = prijevod.lstrip()
    return prijevod.capitalize()

print "Prevodilac HRV u ZG satru\nAutor: Fran Raknic\n\n"
print prevodi(raw_input("Za prevesti:\n")) + "\n"
raw_input()