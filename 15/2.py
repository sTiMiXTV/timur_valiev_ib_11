def num_digits(number):
    result = 1
    while number >= 10:
        number /= 10
        result += 1
    return result

print(num_digits(157))
