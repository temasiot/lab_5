from math import sqrt


def func(a, b, c):
    return a**2+b**2-c**2


if __name__ == "__main__":
    x, y = map(float, input().split())
    print((func(x*y, x**2, y**2) - func(1, x, y)**2) / (1+func(sqrt(x), y**2, 1)))
