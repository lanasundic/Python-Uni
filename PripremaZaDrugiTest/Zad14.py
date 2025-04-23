'''
14. Napisati program koji okreće redosljed karaktera u riječima unutar unijetog stringa. Na 
primjer, ako je dat string „Programski jezik Python“, rezultat je: „iksmargorP kizej nohtyP“.
'''

tekst = input("Unesite string: ")

rijeci = tekst.split()  #splitovanje rijeci po razmacima i pretvaramo u listu
obrnuteRijeci = [i[::-1] for i in rijeci]  #i kao jedna rijec

rezultat = " ".join(obrnuteRijeci)
print("Obrnute riječi su:", rezultat)