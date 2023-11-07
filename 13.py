'''
for x in range(5):
    if (x == 0) or (x == 4):
        print ("X "*6)
    else:
        print ("X"," "*7,"X")
'''


for cislo_radku in range(6):
    for cislo_sloupce in range(5):
        if cislo_radku == 0 or cislo_radku == 5 or cislo_sloupce == 0:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print("X")
