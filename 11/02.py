cifri = input()
cifri_spl = cifri.split()
otvet = [int(cifri_spl[i]) * "*" for i in range(len(cifri_spl))]
for i in otvet:
    print(i)