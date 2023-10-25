def S0(k, N):
    S = 0
    for i in range(k, N+1):
        S += i**2/(k**2+N**2)
    return S


def S1(k, N, i):
    if i > N:
        return 0
    else:
        return i**2/(k**2+N**2) + S1(k, N, i + 1)


def S2(k, N, i):
    if i < k:
        return 0
    else:
        return i**2/(k**2+N**2) + S2(k, N, i - 1)


def S3(k, N, i, t):
    t = t + i**2/(k**2+N**2)
    if i >= N:
        return t
    else:
        return S3(k, N, i+1, t)


def S4(k, N, i, t):
    t = t + i**2/(k**2+N**2)
    if i <= k:
        return t
    else:
        return S4(k, N, i - 1, t)


k, N = map(int,input().split())
print("(iter) S0 = ", S0(k, N))
print("(rec up ++) S1 = ", S1(k, N, k))
print("(rec up --) S2 = ", S2(k, N, N))
print("(rec down ++) S3 = ", S3(k, N, k, 0))
print("(rec down --) S4 = ", S4(k, N, N, 0))
