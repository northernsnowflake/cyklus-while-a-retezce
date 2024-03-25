text = """
Text písně by mělo jít jednoduše vyměnit za jiný.

Postup:

Na začátku nastav počet nalezených písmen na 0.
Pro každý znak textu:
Když znak není obsažen v ! " # $ % & …:
Zvyš počet nalezených písmen o 1.
Vypiš počet nalezených písmen.
"""
nepocitat_znaky = "!#$%&\'()*+,-./:;<=>?@[\\]^_{|}~ \n."

pocet = 0
for znak in text:
    if znak not in nepocitat_znaky:
        pocet = pocet + 1
print(pocet)
