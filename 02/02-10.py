num1 = float(input('Enter a number: '))
num2 = float(input('Enter another number: '))
operation = input('Enter an operation: ')
if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num2 - num1)
elif operation == '*':
    print(num1 * num2)
elif operation == '/' and num2 == 0:
    print(888888)
else: print(num1 / num2)