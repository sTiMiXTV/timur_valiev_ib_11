bibletiok = int(input())
kniga = int(input())
sin = set()
for i in range(bibletiok):
    nov = input()
    sin.add(nov)
for i in range(kniga):
    kop = input()
    if kop in sin:
        print("да")
    else:
        print("нет")
