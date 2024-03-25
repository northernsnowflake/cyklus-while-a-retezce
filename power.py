"""Pomocí cyklu for napiš program, který vypíše:

0 na druhou je 0
1 na druhou je 1
2 na druhou je 4
3 na druhou je 9
4 na druhou je 16
"""

a = range(0,5)
for power in a:
    print(power,' na druhou je ',power**2)
