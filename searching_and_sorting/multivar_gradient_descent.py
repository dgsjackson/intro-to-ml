import math

def f_1(x): return (x[0] - 1)**2 + 3*x[1]**2
def f_2(x): return x[1]**2 + x[1]*math.cos(x[0])
def f_3(x): return (x[0] - 1)**2 + 3*(x[1] - 2)**2 + 4*(x[2] + 1)**2
def f_4(x): return x[0]**2 + 3*x[1]**2 + 4*x[2]**2 + math.cos(x[0]*x[1]*x[2])

def f_1_grad(x): return [ 2*x[0] - 2, 6*x[1] ]
def f_2_grad(x): return [ -x[1]*math.sin(x[0]),  2*x[1] + math.cos(x[0]) ]
def f_3_grad(x): return [ 2*x[0] - 2, 6*x[1] - 12, 8*x[2] + 8 ]
def f_4_grad(x): return [ 2*x[0] - x[1]*x[2]*math.sin(x[0]*x[1]*x[2]), 6*x[1] - x[0]*x[2]*math.sin(x[0]*x[1]*x[2]), 8*x[0]*x[1]*math.sin(x[0]*x[1]*x[2]) ]

max_iter = 10000000

def gradient_descent(f, f_deriv, initial, learning_rate):
    print(f"Running gradient descent with initial x = {initial}")
    table = [["n", "x", "gradient at x", "f(x)"]]
    gradient = f_deriv(initial)
    n = 1
    x = initial
    table.append([n, initial, gradient, f(x)])
    while gradient_not_flat(gradient, 4):
        n += 1
        delta_x = scalar_multiply(gradient, learning_rate)
        x = minus(x, delta_x)
        gradient = f_deriv(x)
        table.append([n, x, gradient, f(x)])
        if (n == max_iter):
            break

    print_results(table)

def gradient_not_flat(gradient, rounding):
    return any(map(lambda x: round(x, rounding) != 0, gradient))

def scalar_multiply(v, k):
    return list(map(lambda x: x*k, v))

def minus(x, y):
    return list(map(lambda a, b: a - b, x, y))

#just print header + last 5 results
def print_results(table):
    print(table[0])
    for row in table[-5:]:
        print(row)

#for f_1 and f_2
# for x in range(-5, 6):
#     for y in range(-5, 6):
#         try:
#             gradient_descent(f_2, f_2_grad, [x, y], 0.01)
#         except OverflowError:
#             print("Encountered overflow error... gradient descent fell off a cliff")
#         print("\n")

#for f_3 and f_4
for x in range(-1, 2):
    for y in range(-1, 2):
        for z in range(-1, 2):
            try:
                gradient_descent(f_3, f_3_grad, [x, y, z], 0.01)
            except OverflowError:
                print("Encountered overflow error... gradient descent fell off a cliff")
            print("\n")