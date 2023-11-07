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
