kol = int(input())
recept = []
for i in range(kol):
    word = input()
    if "лук" not in word:
        recept.append(word)
print(*recept, sep=",")