def space_game(text):
    space = 0
    for i in text:
        if i in " ":
            space += 1
    if space % 2 == 0 and space != 0:
        print("вы выиграли!")
    else:
        print('вы проиграли!')
