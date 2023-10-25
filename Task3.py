from math import cos
from math import sin
from math import e
from math import sqrt


def s(x):
    if abs(x) >= 1 or x == 0:
        return (cos(x)**2+1)/e**x
    else:
        a = 2*x
        s = a
        for k in range(1, 5):
            a *= 4*x**2/(2*k)*(2*k+1)
            s += a
        return s/sin(2*x)


tp, tk, n = map(float, input().split())
dt = (tk-tp)/n
t = tp
while t <= tk:
    s(2*t+1)+2*s(t**2)+sqrt(s(1))
    t += dt
