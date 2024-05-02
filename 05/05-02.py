stroka = int(input("Enter a string: "))
nach = False
for i in range(stroka - 1):
    text = input("Enter a text: ")
    if ("кот" or "Кот") in text:
        text = input("Enter a text: ")
        nach = True
if nach == True:
    print("МЯУ")
else: print("НЕТ")




