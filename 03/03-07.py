begin = 1
end = 1000
popitka = 1
while popitka <=10:
    number = (begin + end) // 2
    print(number)
    choice = input(">, < или = ? ")
    if choice == '>':
        begin = number + 1
    if choice == '<':
        end = number - 1
    if choice == '=':
        print("Угадали за", popitka, "попыток")
        break
    popitka += 1
