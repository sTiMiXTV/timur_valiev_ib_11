word = input()
wordlop = word.split()
otvet = [wordlop[3*i-1] for i in range(1, len(wordlop) // 3 + 1 )]
print(" ".join(otvet))