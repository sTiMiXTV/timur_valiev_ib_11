slovar = {}
for i in range(int(input())):
    inp = input().split(' ')
    key = inp[0]
    val = ' '.join(inp[1:])
    slovar[key] = val
for o in range(int(input())):
    slov = input()
    if slov in slovar:
        print(slovar[slov])
    else:
        print("нету в словаре")