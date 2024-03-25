#for x in range(5):
#    print (x*0,x*1,x*2,x*3,x*4)
"""
Napiš program, který vypíše „tabulku“ s násobilkou.

0       0       0       0       0
0       1       2       3       4
0       2       4       6       8
0       3       6       9       12
0       4       8       12      16
K oddělení sloupců použij znak tabulátoru.

Tabulka je podobná předchozí, jen má v každé "buňce" hodnotu "číslo řádku × číslo sloupce"
"""

for x in range(5):
    for y in range(5):
        print (x*y, end='   ')
    print()
