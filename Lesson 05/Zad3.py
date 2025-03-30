#pretvaranje stringa iz snake_casea u camelCase.
#nacin zapisivanja je to, npr snake_case svake sljedeca rijec se odvaja sa _ a u camelCase se veliko slovo stavi
#npr. moj_broj_telefona i mojBrojTelefona

#iz struktura ili moze i principa isti zadaci za vjezbu kao i iz pajtona - drugoj grupi bilo je obrnuto
    
tekst = input()
rijeci = tekst.split("_")
camel_case = rijeci[0] + "".join(word.capitalize() for word in rijeci[1:])
print(camel_case)
