n = int(input())
result = []
for _ in range(n):
    cubes = [int(x) for x in input().split(' ')]
    big = 999999
    cubes_final = []

    while len(cubes) > 0:
        first, last = cubes[0], cubes[-1]
        if first > big and last > big:
            result.append('НЕТ')
            break
        else:
            if first == big:
                big = cubes.pop(0)
            elif last == big:
                big = cubes.pop(-1)
            elif first < big:
                big = cubes.pop(0)
            elif last < big:
                big = cubes.pop(-1)
            cubes_final.append(str(big))
        if len(cubes) <= 0:
            result.append(' '.join(cubes_final))

for s in result:
    print(s)