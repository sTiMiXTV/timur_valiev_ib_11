def translate(text):
    global translated_text

    remove = 'АЕЁИОУЫЭЮЯаеёиоуыэюя,.!?:;-'
    
    words = text.split(' ')
    new_words = list()
    for i in range(len(words)):
        word = words[i]
        for s in remove:
            word = word.replace(s, '')
        if len(word) > 0:
            new_words.append(word)
    
    translated_text = ' '.join(new_words)

translated_text = None
translate("Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно небольшой тренировки - и вы сможете это делать.")

print(translated_text)
print(translated_text == "двтльнй фкт н ткст н зк НРЗБРЧВ кзвтс двльн прст чтть Дсттчн нбльшй трнрвк в смжт т длть")
