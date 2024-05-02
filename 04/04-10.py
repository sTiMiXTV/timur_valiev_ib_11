chislo = int(input("Enter your chislo: "))
for i in range(17):
    if i % chislo == 0:
        print(chislo, "Да")
        chislo = int(input("Enter your chislo: "))
    else:
        print(chislo, "Нет")
        chislo = int(input("Enter your chislo:"))
