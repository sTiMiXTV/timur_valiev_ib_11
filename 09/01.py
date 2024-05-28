kol = int(input())
shop = []
for i in range(kol):
    sell = input()
    shop.append(sell)
print(*shop, sep="\n")