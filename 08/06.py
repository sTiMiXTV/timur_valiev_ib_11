kol = int(input())
max = int(input())
news = []
for i in range(kol):
    slogon = input()
    if max >= len(slogon):
        news.append(slogon[:max] + '...')
    else:
        news.append(slogon)
print(*news, sep = "\n")