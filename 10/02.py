n = int(input())
ocenki = []
for i in range(n):
    ocenki.append(input())
for o in ocenki:
    print(o)
print()
for o in ocenki:
    if o[-1] in ['4', '5']:
        print(o)
