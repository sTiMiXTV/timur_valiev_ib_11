chislo = int(input('Chislo: '))
delitel = 1
for i in range(chislo + 1):
    if chislo % delitel == 0:
        print(delitel, end=" ")
        delitel += 1
    else:
        delitel += 1
print(end='\n')
if not(chislo /2)  and not(chislo/3) and chislo /chislo:
    print("Простое")
else:
    print("Нет")