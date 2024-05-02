borya = (input("Enter your borya: "))
vova = (input("Enter your vova: "))
dima = (input("Enter your dima: "))
if borya > vova and borya>dima:
    if vova > dima :
        print(borya, vova, dima)
    else: print(borya, dima,vova)
elif vova > borya and vova>dima:
    if borya > dima :
        print(vova, borya, dima)
    else:print(vova, dima, borya)
elif dima > borya and dima>vova:
    if borya > vova:
        print(dima, borya, vova)
    else:print(dima, vova,borya)