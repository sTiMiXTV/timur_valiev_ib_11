chislo1= int(input("Enter your chislo: "))
chislo2= int(input("Enter your chislo: "))
for i in range(chislo1,chislo2 + 1):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)