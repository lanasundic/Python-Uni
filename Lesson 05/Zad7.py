#u rastucem poretku, znaci od najranijeg do najkasnijeg datuma sortirati

datumi = ["21.3.2025", "5.5.2002", "9.12.2025", "1.1.2025"]

def pom(x):
    dan, mjesec, godina = x.split(".")
    return int(godina), int(mjesec), int(dan)

datumi.sort(key = pom)
print(datumi)
