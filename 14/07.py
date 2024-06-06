def print_statistics(arr):
    print(len(arr))
    print(sum(arr) / len(arr))
    print(min(arr))
    print(max(arr))
    n = len(arr)
    s = sorted(arr)
    print((s[n // 2 - 1] / 2.0 + s[n // 2] / 2.0, s[n // 2])[n % 2])