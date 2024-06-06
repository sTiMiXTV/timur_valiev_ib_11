full = input().split(' ')
stack = []
for s in full:
    if s.isdigit():
        stack.append(int(s))
    else:
        b, a = stack.pop(), stack.pop()
        res = 0
        if s == '+':
            res = a+b
        if s == '-':
            res = a-b
        if s == '*':
            res = a*b
        stack.append(res)

print(stack.pop())
