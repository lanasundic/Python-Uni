#1. Napisi funkciju koja uzima recenicu kao ulaz i vraca recenicu sa svakom rijecju obrnutom:
#input: "Hello world"
#output: "olleH dlrow"

n = str(input("Unesite recnicu:"))
l = n.split()

i = 0
for c in l:
    l[i] = c[::-1]
    i += 1

print (" ".join(l))