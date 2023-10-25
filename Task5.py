import inspect
from inspect import getouterframes, currentframe


def func(q, w, deep):
    global deep_f
    deep.append(len(getouterframes(currentframe())))
    if q == w:
        return 1
    elif w == 0:
        return 1
    elif q > 0:
        deep_f = max(deep)
        return func(q-1, w-1, deep) + func(q-1, w, deep)


if __name__ == "__main__":
    n, k = map(int, input().split())
    deep_f = 0
    print(func(n, k, []), deep_f)
