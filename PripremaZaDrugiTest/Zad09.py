#9. Napisati funkciju povrsina_i_obim_kruga(poluprecnik) koja izračunava i vraća površinu
#i obim kruga sa datim poluprečnikom.

obim = 0
povrsina = 0
def povrsina_i_obim_kruga(poluprecnik):
    obim = 2 * poluprecnik * 3.14
    povrsina = poluprecnik**2 * 3.14
    return obim, povrsina

poluprecnik = float(input("Unesite poluprecnik kruga: "))

print(povrsina_i_obim_kruga(poluprecnik))