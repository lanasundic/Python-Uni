#5. Napisati program koji za unijetu masu u kilogramima i visinu u centimetrima, računa Body 
#Mass Index (BMI) osobe. Jedinica za BMI je kg/m2. Opseg BMI koji se smatra zdravim je 
#od 18.5 do 24.9.

kg = float(input("Unesite svoju tezinu u kilogramima: "))
visina = float(input("Unesite svoju visinu u centimetrima: "))
visinaM = visina / 100   

bmi = 0
bmi = kg / (visinaM ** 2)

print("Vas BMI je: ", round(bmi))

if 18.5 <= bmi <= 24.9:
    print("BMI vam je u zdravom opsegu.")
else:
    print("Vas bmi nije u zdravom opsegu.")
