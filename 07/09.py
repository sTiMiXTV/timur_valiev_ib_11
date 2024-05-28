word = input()
cifra = int(input())
if len(word) < cifra:
    print("ошибка")
else:
    print(word[cifra - 1])