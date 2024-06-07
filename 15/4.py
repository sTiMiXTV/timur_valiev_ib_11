def average(values):
    if len(values) == 0:
        return 0
    return sum([x for x in values]) / len(values)

print(average([-5, 2]))
