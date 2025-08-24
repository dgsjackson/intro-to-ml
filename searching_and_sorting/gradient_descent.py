import math

# def f_1(x): return x**2 + x + 1
# def f_2(x): return x**3 - x**4 - x**2
# def f_3(x): return math.sin(x)/(1 + x**2)
# def f_4(x): return 3*math.cos(x) + x**2*math.exp(math.sin(x))

def f_1_deriv(x): return 2*x + 1
def f_2_deriv(x): return 3*x**2 - 4*x**3 - 2*x
def f_3_deriv(x): return (math.cos(x)*(1 + x**2)-2*x*math.sin(x))/(1 + x**2)**2
def f_4_deriv(x): return (-3)*math.sin(x) + 2*x*math.exp(math.sin(x)) + x**2*math.exp(math.sin(x))*math.cos(x)

max_iter = 10000000

def gradient_descent(f_deriv, initial, learning_rate):
    print(f"Running gradient descent with initial x = {initial}")
    table = [["n", "x", "slope at x", "learning rate x slope"]]
    slope = f_deriv(initial)
    n = 1
    x = initial
    table.append([n, initial, slope, learning_rate * slope])
    while round(slope, 4) != 0:
        n += 1
        delta_x = slope * learning_rate
        x = x - delta_x
        slope = f_deriv(x)
        table.append([n, x, round(slope, 4), delta_x])
        if (n == max_iter):
            break

    print_results(table)

#just print header + last 5 results
def print_results(table):
    print(table[0])
    for row in table[-5:]:
        print(row)

for initial in (x * 0.1 for x in range(-20, 20)):
    try:
        gradient_descent(f_1_deriv, initial, 0.01)
        #gradient_descent(f_2_deriv, initial, 0.01)
        #gradient_descent(f_3_deriv, initial, 0.01)
        #gradient_descent(f_4_deriv, initial, 0.01)
    except OverflowError:
        print("Encountered overflow error... gradient descent fell off a cliff")
    
    
    print("\n")
