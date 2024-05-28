kol = int(input())
word = []
for i in range(kol):
    slov = input()
    word.append(slov)
n = int(input())
for j in word:
    if n <= len(j):
        print(j[n - 1], end="")