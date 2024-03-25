
'''

Pomocí cyklů for a příkazu if napiš program, který z jednotlivých 'X' vypíše:

X X X X X X
X         X
X         X
X         X
X         X
X X X X X X
„Z jednotlivých 'X'“ opět znamená, že každý print vypíše maximálně jedno X.
'''

for cislo_radku in range(6):
    for cislo_sloupce in range(5):
        if cislo_radku == 0 or cislo_radku == 5 or cislo_sloupce == 0:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print("X")
