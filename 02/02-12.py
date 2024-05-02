text1 = input("Enter your text: ")
long = float(len(text1))
rubl = int(long * 40) // 100
kop = int(long * 40) % 100
print( str(rubl) + " р." + str(kop) + " коп.")
