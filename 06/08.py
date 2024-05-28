name = set()
repit = set()
nomer = int(input())
for i in range(nomer):
    imya = input()
    if imya in name:
        repit.add(imya)
    else:
        name.add(imya)
print(len(repit))