cislo = int(input("zadejte cislo: "))
delitel = 0
for i in range(1, 100):
    delitel += 1
vysledek = cislo/delitel == 0
print(vysledek)