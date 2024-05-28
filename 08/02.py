one = input()
two = input()
bulls = 0
cows = 0
for i in range(len(one)):
    if one[i] == two[i]:
        bulls += 1
    else:
        cows += one[i] in two
print(bulls, cows)