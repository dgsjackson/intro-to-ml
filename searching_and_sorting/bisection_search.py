#estimate cuberoot(2): estimate root of f(x) = x^3 - 2
#bisection search

lower = 0
upper = 2
mid = (lower + upper)/2


while (upper - mid > 0.00001):
    f_mid = mid ** 3 - 2
    if (f_mid > 0):
        upper = mid
    else:
        lower = mid
    mid = (lower + upper)/2

print(mid)