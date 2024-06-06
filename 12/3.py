num = [int(x) for x in input().split(' ')]
m, k = [int(x) for x in input().split(' ')]
result = sum([num[i] for i in range(m, k + 1)])
print(result)
