def who_are_you_and_hello():
    while True:
        x = input()
        if x.isalpha() and x[0].istitle() and x[1:].islower():
            break