kol = int(input())
cifri = []
flag = False
for i in range(kol):
    number = int(input())
    cifri.append(number)
summa = int(input())
for j in cifri:
    for o in cifri:
        if j != o and j * o == summa:
            flag = True
if flag == True:
    print("ДА")
else:
    print("НЕТ")