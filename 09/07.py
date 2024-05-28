flak = False
number = int(input())
load = []
load_f = []
for i in range(number):
    load.append(input())
number1 = int(input())
for i in range(number1):
    load_f.append(input())
for i in load:
    for j in load_f:
        if j in i:
            flak = True
        else:
            flak = False
            break
    if flak:
        print(i)