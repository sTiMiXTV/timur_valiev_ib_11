text = " "
war = "Евразия"
mir = "Остазия"
kol_string = int(input("Enter a number: "))
for i in range(kol_string):
    text = input("Enter a text: ")
    if "С кем война ?" in text:
        print(war)
    elif "С кем мир ?" in text:
        print(mir)
    elif "Меняем" in text:
        war, mir = mir, war