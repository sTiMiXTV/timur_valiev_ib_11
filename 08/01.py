word = []
while True:
    kip = input()
    if kip != "стоп":
        word.append(kip)
    else:
        break
max = max(word, key=len)
min = min(word, key=len)
if min in max:
    print("да")
else:
    print("нет")
print(max)
print(min)
print(word)