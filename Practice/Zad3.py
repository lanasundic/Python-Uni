#3. Napisi funkciju koja prima recenicu kao ulaz, a vraca najduzu rijec i njenu duzinu kao integer.
#input: "ja opet skijam"
#output: ("skijam", 6)

s1 = str(input("Unesite recenicu:"))
l1 = s1.split()
najduza = l1[0]

for c in l1:
    if len(c) > len(najduza):
        najduza = c

print(najduza, len(najduza))