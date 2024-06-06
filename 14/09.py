def ask_password():
    i = 0
    while True:
        pas = input()
        if pas == "password" and i != 3:
            print("Пароль принят")
            break
        elif pas != "password" and i != 3:
            i += 1
            if i == 3:
                print("В доступе отказано")
                break
ask_password()