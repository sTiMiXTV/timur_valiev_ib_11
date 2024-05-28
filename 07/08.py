cifra = int(input())
emno = int(str(cifra)[0])
while emno != 1:
    cifra = cifra * emno
    emno = int(str(cifra)[0])
print(cifra)

