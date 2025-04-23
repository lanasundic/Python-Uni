#9. Napisati funkciju povrsina_i_obim_kruga(poluprecnik) koja izračunava i vraća površinu
#i obim kruga sa datim poluprečnikom.

obim = 0
povrsina = 0
def povrsina_i_obim_kruga(poluprecnik):
    obim = 2 * poluprecnik * 3.16
    povrsina = poluprecnik**2 * 3.16

poluprecnik = float(input("Unesite poluprecnik kruga: "))

print(povrsina, obim)