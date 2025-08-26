import matplotlib.pyplot as plot

from objects import mv_euler_estimator as euler

def ds_dt(point):
    return -0.0003 * point[1]["s"]*point[1]["i"]

def di_dt(point):
    return 0.0003 * point[1]["s"]*point[1]["i"] - 0.02 * point[1]["i"]

def dr_dt(point):
    return 0.02 * point[1]["i"]

derivatives = { "s": ds_dt, "i": di_dt, "r": dr_dt }
estimator = euler.MultiEulerEstimator(derivatives)
initial_point = (0, { "s": 1000, "i": 1, "r": 0 })
points = estimator.estimate_points(initial_point, 1, 400)

x = list(map(lambda p: p[0], points))
s = list(map(lambda p: p[1]["s"], points))
i = list(map(lambda p: p[1]["i"], points))
r = list(map(lambda p: p[1]["r"], points))
plot.plot(x, s, label="Susceptible")
plot.plot(x, i, label="Infected")
plot.plot(x, r, label="Recovered")
plot.xlabel("Days")
plot.ylabel("No of People")
plot.legend()
plot.show()