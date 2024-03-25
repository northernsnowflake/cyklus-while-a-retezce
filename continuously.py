"""
Napiš program, který postupně z jednotlivých 'X' vypíše:

X
X X
X X X
X X X X
„Z jednotlivých 'X'“ opět znamená, že každý print vypíše maximálně jedno X.
"""


'''
for z in range(1):
    for x in range(2):
        for y in range(1):
            print ('X', end=' ')
        print()
        print ('X', end=' ')
    print ('X X')
print ('X X X X', end=' ')
'''

pocet_radku = 4
for i in range(1,pocet_radku+1):
    print('X '*i, end = '\n')

print('-----')
n=4
for radek in range(1,n+1):
    for sloupec in range(radek):
        print('X', end = ' ')
    print()


"""

print('-----')
pocet = int(input('Zadej počet řádků: '))
for x in range(pocet):
    if (x == 0) or (x == [-3]):
        print ("X "*6)
    else:
        print ("X"," "*7,"X")
"""