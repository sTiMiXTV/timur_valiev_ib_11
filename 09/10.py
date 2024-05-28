n = int(input())
numbers = []
for _ in range(n):
  number = int(input())
  numbers.append(number)
p = int(input())
q = int(input())

result = 0
for _ in range(p - 1):
  numbers.pop(0)
for _ in range(q - p + 1):
  result += numbers.pop(0)
print(result)