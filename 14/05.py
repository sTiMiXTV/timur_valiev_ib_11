def triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        print('Это треугольник')
    else:
        print("Это не треугольник")