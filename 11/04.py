number = [int(x) for x in input().split() if int(x) % 2 != 0 and (int(x)**2) % 10 != 9]
print(*[x**2 for x in number])
