import math
from searching_and_sorting import multivar_gradient_descent as mvgd
from supervised import pseudoinverse_regression as pseudo
import numpy as np

#fitting a power regression model using gradient descent
data = [(0.001, 0.01),(2, 4),(3, 9)]

#y = a*x^b
#rss = sum((a*x^b - y)^2)

def power_rss(params):
    rss = 0
    a, b = params
    for x, y in data:
        rss += (a*x**b - y)**2
    return rss

def power_drss(point):
    grad = [0, 0]
    a, b = point
    for x, y in data:
        common = 2*(a*x**b - y) * x**b
        da = common
        db = common * a * math.log(x)
        grad[0] += da
        grad[1] += db

    return grad

initial = [1, 1]
results = mvgd.gradient_descent(power_rss, power_drss, initial, 0.001)
mvgd.print_results(results)
print(f"a = {results[-1][1][0]}, b = {results[-1][1][1]}")
print(f"RSS = {results[-1][-1]}")

#fitting quadratic y = ax^2 + bx + c to the same data as above
#rss = sum((ax^2 + bx + c - y)^2)
def quadr_rss(params):
    rss = 0
    a, b, c = params
    for x, y in data:
        rss += (a*x**2 + b*x + c - y)**2
    return rss

def quadratic_drss(params):
    grad = [0, 0, 0]
    a, b, c = params
    for x, y in data:
        common = 2*(a*x**2 + b*x + c - y)
        da = common*x**2
        db = common*x
        dc = common
        grad[0] += da
        grad[1] += db
        grad[2] += dc

    return grad

initial = [0, 0, 0]
results = mvgd.gradient_descent(quadr_rss, quadratic_drss, initial, 0.001)
mvgd.print_results(results)
print(f"a = {results[-1][1][0]}, b = {results[-1][1][1]}, c = {results[-1][1][2]}")
print(f"RSS = {results[-1][-1]}")

#fit model using pseudoinverse for comparison
x_values = np.array([p[0] for p in data])
design = np.array([(x_values ** i) for i in range(3)]).transpose()
obs = np.array([p[1] for p in data])
_, _, rss = pseudo.pseudoinv_regression(design, obs)
print(f"RSS from pseudoinverse regression = {rss}")

#fitting y = 5/(1 + exp(-(ax + b))) + 0.5
data = [(1, 1),(2, 1),(3, 2)]

def logistic_rss(params):
    rss = 0
    a, b = params
    for x, y in data:
        rss += (5/(1 + math.exp(-(a*x + b))) + 0.5 - y)**2
    return rss

def logistic_drss(params):
    grad = [0, 0]
    a, b = params
    for x, y in data:
        common = 2*(5/(1 + math.exp(-(a*x + b))) + 0.5 - y) * 5*math.exp(-(a*x + b))/(1 + math.exp(-(a*x + b)))**2
        da = common * x
        db = common
        grad[0] += da
        grad[1] += db
    return grad

initial = [0, 0]
results = mvgd.gradient_descent(logistic_rss, logistic_drss, initial, 0.001)
mvgd.print_results(results)
print(f"a = {results[-1][1][0]}, b = {results[-1][1][1]}")
print(f"RSS = {results[-1][-1]}")

#fit model using pseudoinverse for comparison
def transform_y(y):
    return -math.log(5/(y - 0.5) - 1)

x_values = np.array([p[0] for p in data])
design = np.array([(x_values ** i) for i in range(2)]).transpose()
obs = np.array([transform_y(p[1]) for p in data])
_, _, rss = pseudo.pseudoinv_regression(design, obs)
print(f"RSS from pseudoinverse regression = {rss}")

#Fiting y = a*sin(bx) + c*sin(dx)
#cant fit using pseudoinverse due to non linearizable in parameters
data = [(0, 0), (1, -1), (2, 2), (3, 0), (4, 0),(5, 2), (6, -4), (7, 4), (8, 1), (9, -3)]

def rss_f4(params):
    a, b, c, d = params
    rss = 0
    for x, y in data:
        rss += (a*math.sin(b*x) + c*math.sin(d*x) - y)**2
    return rss

def drss_f4(params):
    a, b, c, d = params
    grad = [0, 0, 0, 0]
    for x, y in data:
        common = 2*(a*math.sin(b*x) + c*math.sin(d*x) - y)
        drss_da = common * math.sin(b*x)
        drss_db = common * a*x*math.cos(b*x)
        drss_dc = common * math.sin(d*x)
        drss_dd = common * c*x*math.cos(d*x)
        grad[0] += drss_da
        grad[1] += drss_db
        grad[2] += drss_dc
        grad[3] += drss_dd
    return grad

initial = [1.4035920124040446, 2.026198976315889, 2.697267449786242, -2.3559623245552226]
results = mvgd.gradient_descent(rss_f4, drss_f4, initial, 0.0001)
mvgd.print_results(results)
# try a bunch of different initial points
# for a in range(-2, 3):
#     for b in range(-2, 3):
#         for c in range(-2, 3):
#             for d in range(-2, 3):
#                 initial = [a, b, c, d]
#                 results = mvgd.gradient_descent(rss_f4, drss_f4, initial, 0.001)
#                 print(results[-1])