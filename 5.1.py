from math import sqrt


def g(a, b, c):
    return a**2+b**2-c**2


x, y = map(float, input().split())
print((g(x*y, x**2, y**2) - g(1, x, y)**2) / (1+g(sqrt(x), y**2, 1)))
