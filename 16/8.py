printed = list()

def print_only_new(message):
    global printed
    if message not in printed:
        printed.append(message)
        print(message)

print_only_new('Шутка номер 15')
print_only_new('Шутка номер 23')
print_only_new('Шутка номер 24')
print_only_new('Шутка номер 24')
print_only_new('Шутка номер 100')
print_only_new('Шутка номер 24')
print_only_new('Шутка номер 99')
print_only_new('Шутка номер 15')
print_only_new('Шутка номер 100')
