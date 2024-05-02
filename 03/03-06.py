parol1 = input("Ведите пароль: ")
dl_parol1 = len(parol1)
parol2 = input("Повторите пароль: ")
dl_parol2 = len(parol2)

while dl_parol1 < 8:
    print("Короткий!")
    break
while parol1 != parol2:
    print("Различаются.")
    break
if "123" in parol1 :
    print("Простой!")
else:
    while dl_parol1 > 8 and parol1 == parol2:
        print("ОК")
        break