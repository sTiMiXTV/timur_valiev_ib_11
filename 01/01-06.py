print("Умеете ли Вы рабоать в Python?")
word1 = input("Enter a word, да или нет: ")
print("Умеете ли Вы создавать сайты ? ")
word2 = input("Enter a word, да или нет ")

if word1 == "да" and word2 == "да":
    print("Вы выдающийся программист!!!")
elif word1 == "да" and word2 == "нет":
    print ("Вы хороший сотрудник, но вы желаете научиться создавать сайты ? ")
elif word1 == "нет" and word2 == "да":
    print("Мы вас подтянем вопросы")
elif word1 == "нет" and word2 == "нет":
    print("Не переживай, мы всему тебя обучим")
else: print("Ошибка!!!")