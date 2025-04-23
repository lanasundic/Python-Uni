#2. Napisati funkciju sabiraj(n) koja vraća sumu kubova prirodnih brojeva od 1 do n.

def sabiraj(n):
    for i in range(1, n + 1):
        s += i*i*i

n = int(input("Unesite n: "))
print(f"Zbir kubova od 1 do {n} je: {sabiraj(n)}")