def larger_root(p, q):
    d = discriminant(1, p, q)
    return (-p + d**0.5) / 2

def smaller_root(p, q):
    d = discriminant(1, p, q)
    return (-p - d**0.5) / 2

def discriminant(a, b, c):
    return b**2 - 4*a*c

def main():
    p, q = float(input()), float(input())
    print(discriminant(1, p, q))
    print(smaller_root(p, q), larger_root(p, q))

main()
