stolov = set()
nebilo = set()
nomer = int(input())
for i in range(nomer):
    eda = input()
    stolov.add(eda)
nomer = int(input())
for u in range(nomer):
    lop = int(input())
    for l in range(lop):
        eda = input()
        nebilo.add(eda)
pok = stolov - nebilo
print(*pok, sep='\n')