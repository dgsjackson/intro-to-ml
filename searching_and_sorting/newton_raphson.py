#estimate cuberoot(2): estimate root of f(x) = x^3 - 2
#Newton Raphson: estimate root via tangent lines

estimate = 2
last_estimate = None

while last_estimate == None or round(estimate, 6) != round(last_estimate, 6):
    f = estimate ** 3 - 2
    slope = 3 * (estimate ** 2)
    tangent_root = estimate - (f / slope)
    last_estimate = estimate
    estimate = tangent_root

print(estimate)