def take_large_banknotes(banknotes):
    return [x for x in banknotes if x > 10]

print(*take_large_banknotes([1, 5, 500, 0.5, 2, 0.1, 10, 100, 100, 1000, 50]))
