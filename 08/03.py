nick = input()
for i in nick:
    if i not in 'qwertyuiopasdfghjklzxcvbnm1234567890_':
        print('Неверный символ:', i)
        break
else:
    print('OK')