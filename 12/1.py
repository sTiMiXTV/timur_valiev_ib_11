n = int(input())
result = []
for i in range(n):
  strok = input()
  index = strok.find('кот')
  if index != -1:
    result.append(str(i + 1) + ' ' + str(index + 1))
for s in result:
  print(s)