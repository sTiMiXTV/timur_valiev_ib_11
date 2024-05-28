col = int(input())
gooool = []
for i in range(col):
    slovo = input()
    if "%%" in slovo:
        gooool.append(slovo[2:])
        continue
    if "####" in slovo:
        continue
    else:
        gooool.append(slovo)
print(*gooool, sep="\n")