slovar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
size = int(input())
for y in range(size):
  for x in range(size):
    bukva = slovar[x]
    cifra = str(size - y)
    print(bukva + cifra, end=' ')
  print()