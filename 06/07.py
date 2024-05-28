kil = int(input())
ura = set()
diff = set()
for i in range(kil):
    frik = int(input())
    lop = set()
    for a in range(frik):
        name = input()
        if i == 0:
            ura.add(name)
        elif name in ura:
            lop.add(name)
    ipa = ura.intersection(lop)
print(ipa)
