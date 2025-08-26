import math
import matplotlib.pyplot as plot
from objects import mv_euler_estimator as euler

V_Na = 115
V_K = -12
V_L = 10.6
g_hat_Na = 120
g_hat_K = 36
g_hat_L = 0.3
g_L = g_hat_L

def alpha_n(V):
    return 0.01 * (10 - V)/(math.exp(0.1 * (10 - V)) - 1)

def alpha_m(V):
    return 0.1 * (25 - V)/(math.exp(0.1 * (25 - V)) - 1)

def alpha_h(V):
    return 0.07 * math.exp(-V/20)

def beta_n(V):
    return 0.125 * math.exp(-V/80)

def beta_m(V):
    return 4 * math.exp(-V/18)

def beta_h(V):
    return 1/(math.exp(0.1 * (30 - V)) + 1)

V_0 = 0
n_0 = alpha_n(V_0)/(alpha_n(V_0) + beta_n(V_0))
m_0 = alpha_m(V_0)/(alpha_m(V_0) + beta_m(V_0))
h_0 = alpha_h(V_0)/(alpha_h(V_0) + beta_h(V_0))

intial_point = (0, {"V": V_0, "n": n_0, "m": m_0, "h": h_0})

def dn_dt(point):
    V = point[1]["V"]
    n = point[1]["n"]
    return alpha_n(V)*(1 - n) - beta_n(V)*n

def dm_dt(point):
    V = point[1]["V"]
    m = point[1]["m"]
    return alpha_m(V)*(1 - m) - beta_m(V)*m

def dh_dt(point):
    V = point[1]["V"]
    h = point[1]["h"]
    return alpha_h(V)*(1 - h) - beta_h(V)*h

def g_Na(m, h):
    return g_hat_Na * m**3 * h

def g_K(n):
    return g_hat_K * n**4

def I_Na(V, m, h):
    return g_Na(m, h) * (V - V_Na)

def I_K(V, n):
    return g_K(n) * (V - V_K)

def I_L(V):
    return g_L * (V - V_L)

def s(t):
    if (t >= 10 and t <= 11 or
        t >= 20 and t <= 21 or
        t >= 30 and t <= 40 or
        t >= 50 and t <= 51 or
        t >= 53 and t <= 54 or
        t >= 56 and t <= 57 or
        t >= 59 and t <= 60 or
        t >= 62 and t <= 63 or
        t >= 65 and t <= 66):
        return 150
    else:
        return 0

def dV_dt(point):
    t = point[0]
    V = point[1]["V"]
    n = point[1]["n"]
    m = point[1]["m"]
    h = point[1]["h"]
    return s(t) - I_Na(V, m, h) - I_K(V, n) - I_L(V)

derivatives = { "V": dV_dt, "n": dn_dt, "m": dm_dt, "h": dh_dt }
estimator = euler.MultiEulerEstimator(derivatives)
points = estimator.estimate_points(intial_point, 0.01, 8000)

t = list(map(lambda p: p[0], points))
s_t = list(map(lambda t: s(t), t))
V_t = list(map(lambda p: p[1]["V"], points))

plot.plot(t, s_t, label="Stimulus")
plot.plot(t, V_t, label="Voltage")
plot.xlabel("Time (ms)")
plot.ylabel("Voltage")
plot.legend()
plot.show()