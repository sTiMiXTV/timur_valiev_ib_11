kol_strok = int(input("Kol strok: "))
kol_stars = 1
probel = 10
while kol_strok > 0:
    print(" " * probel, "*" * kol_stars)
    probel -= 1
    kol_stars += 2
    kol_strok -= 1
