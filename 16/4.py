receipt_num = 1
item_names = list()
item_costs = list()

def add_item(item_name, item_cost):
    global item_names, item_costs
    item_names.append(item_name)
    item_costs.append(item_cost)

def print_receipt():
    global receipt_num
    if len(item_names) > 0:
        print(f'Чек {receipt_num}. Всего предметов: {len(item_names)}')
        for i in range(len(item_names)):
            print(f'{item_names[i]} - {item_costs[i]}')
        print(f'Итого: {sum(item_costs)}')
        print('-----')

        receipt_num += 1
        item_names.clear()
        item_costs.clear()

add_item('Блокнот', 100)
print_receipt()

add_item('Ручка', 70)
print_receipt()
print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)
add_item('Чай', 5)
print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)
# (Отменить чек) - этот чек не печатаем
