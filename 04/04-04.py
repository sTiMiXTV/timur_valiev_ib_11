chislo = int(input("Enter your chislo: "))
facktorial = 1
n = 1
for i in range(chislo):
    facktorial *= n
    n+=1
print(facktorial)