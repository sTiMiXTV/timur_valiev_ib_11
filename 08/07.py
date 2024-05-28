n = int(input())
result = []
for i in range(n):
  strok = input()
  for j in range(1, 1 + len(strok)):
    if (1 + len(strok) - j) >= 3 and strok[j:j+3] == 'кот':
      result.append(str(i + 1) + ' ' + str(j + 1))
      break
for s in result:
  print(s)