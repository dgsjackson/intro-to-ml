import math
from searching_and_sorting import multivar_gradient_descent as mvgd

data = [
    (0, 0, 0, 0.0), (1, 0, 0, 0.2), (2, 0, 0, 0.5), (0, 1, 0, 0.4), 
    (0, 2, 0, 0.6), (0, 0, 1, 0.5), (0, 0, 2, 0.8), (1, 1, 0, 1.0), 
    (1, 0, 1, 0.0), (0, 1, 1, 0.1)
]

#fitting to logistic model with interactions
# y = 1/(1 + e^(-u)) where u = a1x1 + a2x2 + a3x3 + a12x1x2 + a13x1x3 + a23x2x3 + b

def u(params, point):
    a1, a2, a3, a12, a13, a23, b = params
    x1, x2, x3, _ = point
    return a1*x1 + a2*x2 + a3*x3 + a12*x1*x2 + a13*x1*x3 + a23*x2*x3 + b

def drss(params):
    grad = [0] * 7
    for point in data:
        x1, x2, x3, y = point
        e_u = math.exp(-u(params, point))
        common = 2*(1/(1 + e_u) - y)*(e_u/(1 + e_u)**2)
        drss_da1 = common * x1
        drss_da2 = common * x2
        drss_da3 = common * x3
        drss_da12 = common * x1*x2
        drss_da13 = common * x1*x3
        drss_da23 = common * x2*x3
        drss_db = common
    
        grad[0] += drss_da1
        grad[1] += drss_da2
        grad[2] += drss_da3
        grad[3] += drss_da12
        grad[4] += drss_da13
        grad[5] += drss_da23
        grad[6] += drss_db

    return grad

initial = [1, 1, 1, 1, -1, -1, -1]
results = mvgd.gradient_descent(None, drss, initial, 0.001)
mvgd.print_results(results)
#[1.016874901465265, 1.34214344870657, 1.909623826054153, 3.8603146769283585, -4.889360986872706, -3.338215362464148, -2.110610840601726]