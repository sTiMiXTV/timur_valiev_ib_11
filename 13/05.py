spisk = {}
for i in range(int(input())):
    name, data, mes = input().split()
    if mes in spisk:
        spisk[mes].append(name)
    else:
        spisk[mes] = [name]
for i in range(int(input())):
    slov = input()
    if slov in spisk:
        print(' '.join(spisk[slov]))
    else:
        print()