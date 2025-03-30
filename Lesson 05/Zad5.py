#Ucitava se string i treba da se provjeri da li je string sljedeceg oblika
#a^n - b^n - c^n
#aaa - bbb - ccc ovo jeste
#aaa - bbb - cc ovo nije
#aaa - bb - ccc ovo nije

#uvijek kad imamo ovakve zadatke da li nesto vazi da li je nesto validno, 
#namjestimo uvijek prvo uslove da je to netacno pa gledamo kad je tacno

s = input()
dobri_smo = False

parts = s.split("-")

i = 0
for part in parts:
    parts[i] = part.strip()
    i += 1
    
if len(parts) != 3:
    print("Ne")
elif len(parts[0]) != len(parts[1]) or len(parts[1]) != len(parts[2]):
    print("Ne")
elif len(set(parts[0])) != 1 or parts[0][0] != 'a':
    print("Ne")
elif len(set(parts[1])) != 1 or parts[1][0] != 'b':
    print("Ne")
elif len(set(parts[2])) != 1 or parts[2][0] != 'c':
    print("Ne")
else:
    print("Da")


#MALO NEJASNO....