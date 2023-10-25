import inspect
from inspect import getouterframes, currentframe


def func(q, w):
    global deep
    deep = max(deep, len(getouterframes(currentframe())))
    if q == w:
        return 1
    elif w == 0:
        return 1
    elif q > 0:
        return func(q-1, w-1) + func(q-1, w)


if __name__ == "__main__":
    n, k = map(int, input().split())
    deep = 0
    print(func(n, k), deep)
