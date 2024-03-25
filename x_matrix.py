#X=('X')

"""
Pomocí cyklů for a parametru end pro print napiš program, který postupně z jednotlivých 'X' vypíše:

X X X X X
X X X X X
X X X X X
X X X X X
X X X X X
„Z jednotlivých 'X'“ znamená, že každý print vypíše maximálně jedno X. Nepoužívej tedy např. print('X X X X X') ani print('X ' * 5).
"""
for x in range(5):
    for y in range(5):
        print ('X', end=' ')
    print()
