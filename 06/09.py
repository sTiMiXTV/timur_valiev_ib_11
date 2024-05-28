ICE = set()
recep = set()
nomer = int(input())
for i in range(nomer):
    ICE.add(input())
namerecepn = int(input())
for i in range(namerecepn):
    namerecep = input()
    enter = int(input())
    flag = True
    for j in range(enter):
        recep.add(input())
    for i in recep:
        if not i in ICE:
            flag = False
    if flag:
        print(namerecep)
    recep = set()