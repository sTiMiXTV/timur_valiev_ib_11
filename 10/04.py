n = int(input())
a = []
for i in range(n):
    a.append(input())
for i in range(n):
    for j in range(i + 1, n):
        if len(a[i]) > len(a[j]):
            a[i], a[j] = a[j], a[i]
        elif a[i] == a[j]:
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
print(*a,sep='\n')