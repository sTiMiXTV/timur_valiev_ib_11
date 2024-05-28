kol_whit = int(input())
white = []
for i in range(kol_whit):
    word = input()
    white.append(word)
kol_searh = int(input())
searh = []
for j in range(kol_searh):
    word = input()
    searh.append(word)
for o in searh:
    if o in white:
        print(o)
