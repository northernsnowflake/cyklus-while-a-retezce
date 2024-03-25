"""
Předchozí programy z této sekce uprav tak, aby počet řádků (či velikost čtverce/trojúhelníku/tabulky) mohl zadat uživatel.
"""

pocet = int(input('Zadej počet řádků: '))

for cislo_radku in range(pocet):
    for cislo_sloupce in range(pocet-1):
        if cislo_radku == 0 or cislo_radku == pocet-1 or cislo_sloupce == 0:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print("X")


'''
for x in range(pocet):
    if (x == 0) or (x == [-3]):
        print ("X "*6)
    else:
        print ("X"," "*7,"X")
'''
"""
Co dělá tenhle kód?
"""


for c in 'Ahoj světe!':
    print(c)

"""

for c in 38:
    print(c)
""" 