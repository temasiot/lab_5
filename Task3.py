from math import cos
from math import sin
from math import e
from math import sqrt
from prettytable import PrettyTable


def s(x):
    if abs(x) >= 1 or x == 0:
        return (cos(x)**2+1)/(e**x)
    else:
        a = 2*x
        s = a
        for k in range(1, 5):
            a *= 4*x**2/(2*k)*(2*k+1)
            s += a
        return s/sin(2*x)


if __name__ == "__main__":
    th = ['t','s']
    table = PrettyTable(th)
    tp, tk, n = map(float, input().split())
    dt = (tk - tp) / n
    t = tp
    while t <= tk:
        f = s(2 * t + 1) + 2 * s(t ** 2) + sqrt(s(1))
        td = []
        td.append(t)
        td.append(f)
        table.add_row(td)
        t += dt
    print(table)