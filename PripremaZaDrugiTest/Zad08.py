'''
8. Napisati funkciju dug(kredit, kamata, broj_mjeseci) koja računa vrjiednost duga za 
kredit nakon datog broja mjeseci sa datom kamatom. Na primjer, ukoliko je vrijednost 
podignutog kredita 10 000 eura i kamata 5%, nakon 10 mjeseci dug će biti 16 288.95 eura. 
'''

def dug(kredit, kamata, broj_mjeseci):
    
mjeseci = int(input("Unesite broj mjeseca: "))
kamata = int(input("Unesite iznos kamate: "))
