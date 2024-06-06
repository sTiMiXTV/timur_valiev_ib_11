buk = input()
pred = input().split(' ')

for word in pred:
    if buk in word.lower():
        print(word)
