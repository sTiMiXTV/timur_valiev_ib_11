number = int(input())
suma = []
for i in range(number):
    cifra = int(input())
    suma.append(cifra)
for j in range(number - 1):
    print(number[j] + number[j+1])