import random

slovo = random.choice(['trávník','stromek','stavení'])
#slovo = random.choice(['čokoláda'])
stav = '_'*len(slovo)
neuspesne = 0
#pocet = len(slovo)
print(stav)

while True:
    pismeno = str(input("Zadej písmeno:"))
    if pismeno in slovo:
        pozice = slovo.index(pismeno)
        zacatek = stav[:pozice]
        konec = stav[pozice + 1:]
        nove_slovo = zacatek + pismeno + konec
        stav = nove_slovo
        #print('elif pismeno in slovo')
        if '_' not in stav:
            print('Gratuluji')
            break
    elif pismeno not in slovo:
        neuspesne = neuspesne + 1
        print(f'neuspesne {neuspesne}')
        continue
    elif pismeno == '':
        neuspesne = neuspesne + 1
        print(f'neuspesne {neuspesne}')
        continue
    elif neuspesne > 9:
        print('Hráč bohužel prohrál')
        break
    print(stav)
