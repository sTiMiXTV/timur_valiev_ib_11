deuclain = set()
english = set()
cifrae = int(input())
cifrad = int(input())
for i in range(cifrae):
    familee = input()
    english.add(familee)
for i in range(cifrad):
    familed = input()
    deuclain.add(familed)
all = deuclain ^ english
allr = len(all)
if all != set():
    print(allr)
else:
    print("no")
