word = list(input().lower().replace(' ', ''))
word.sort()

long = word[0]
for s in word:
    if word.count(s) > word.count(long):
        long = s

print(long)
