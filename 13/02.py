nomer = {}
for _ in range(int(input())):
    cifr, name = input().split()
    if name in nomer:
        nomer[name].append(cifr)
    else:
        nomer[name] = [cifr]
for _ in range(int(input())):
    name = input()
    if name in nomer:
        print(*nomer[name])
    else:
        print('Нет в телефонной книге')
