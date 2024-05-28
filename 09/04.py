kol_mag = int(input())
news = []
for i in range(kol_mag):
    mag = input()
    news.append(mag)
kol_obv = int(input())
for j in range(kol_obv):
    obv = int(input())
    print(news[obv - 1])
