#prevodilac HRV u ZG-SATRA
#autor: Fran Raknic

samoglasnici = ['a','e','i','o','u']
znakovi = ['.',':',';','!','?']

#TODO:
#dodati iznimke za rijeci od 3 slova
#prevodilac satra -> HRV
#formatirati ispis lowercase, capitalize etc.
#formatirati input

#razdvajanje rijeci na slogove
def Fslogovi(rijec):
	rijec = rijec.lower()
	slogovi = []
	if checkRijec(rijec) == False:
		slogovi.append(rijec)
		return slogovi
	else:
		for i in range(0, len(rijec)):
			if rijec[i] in samoglasnici:
				slogovi.append(rijec[:i+1])
				slogovi.append(rijec[i+1:])
				break
		return slogovi
	
def checkRijec(rijec1):
	if len(rijec1) <= 3:
		return False
	else:
		return True

#prevodi prima recenicu, vraca prevedeno	
def prevodi(tekst):
	tmpPrjevod = []
	prjevod = []
	tekst = tekst.split()
	for rijec in tekst:
		tmpPrjevod.append(Fslogovi(rijec))
	for rijec in tmpPrjevod:
		prjevod.append(" ")
		for slog in reversed(rijec):
			prjevod.append(slog)
	prjevod = "".join(prjevod)
	prjevod = prjevod.lstrip()
	return prjevod.capitalize()
	
#testiranje
print "Prevodilac HRV u ZG satru\nAutor: Fran Raknic\n\n"
print "Za izlaz is prevodioca upisite x\n"
print "Unesite tekst za prijevod!\n"

def interface():
	usrinput = raw_input()
	if usrinput == "x":
		print "Izlazim!"
	else:
		print prevodi(usrinput)
		print "." * 20
		interface()
		
interface()
