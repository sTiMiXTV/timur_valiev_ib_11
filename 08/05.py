kol = int(input())
sov = []
for i in range(kol):
    slovo = input()
    if "не" in slovo[0:3] or "Не" in slovo[0:3]:
        sov.append(slovo[3:])
    else:
        sov.append(slovo)
print(*sov, sep = '\n')
