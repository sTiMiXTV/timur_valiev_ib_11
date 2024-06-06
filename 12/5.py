num = int(input()[1:])
prog = []
for _ in range(num):
    s = input().split('#')[0].rstrip()
    prog.append(s)
for s in prog:
    print(s)
