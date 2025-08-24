#estimate nth_root(a)
#IE estimate root of f(x) = x^n - a

#assume n is positive and a >= 1, not sure how to do this otherwise
def calc_root_bisection(a, n, precision):
    f = lambda x: x**n - a
    lower = 0
    upper = a
    mid = (upper + lower) / 2

    while round(mid, precision) != round(upper, precision):
        f_mid = f(mid)
        if f_mid == 0:
            return mid
        if f_mid > 0:
            upper = mid
        else:
            lower = mid
        mid = (upper + lower) / 2

    return round(mid, precision)

def calc_root_newton_raphson(a, n, precision):
    f = lambda x: x**n - a
    f_deriv = lambda x: n * (x ** (n - 1))

    estimate = 2
    last_estimate = None

    while last_estimate == None or round(estimate, precision) != round(last_estimate, precision):
        f_x = f(estimate)
        slope = f_deriv(estimate)
        tangent_root = estimate - (f_x / slope)
        last_estimate = estimate
        estimate = tangent_root

    return round(estimate, precision)