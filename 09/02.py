kol = int(input())
bibl = []
for i in range(kol):
    masiv = input()
    bibl.append(masiv)
search = input()
for j in bibl:
    if search in j:
        print(j)
