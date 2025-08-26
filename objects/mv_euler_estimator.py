import matplotlib.pyplot as plt

#multivariable euler estimator
class MultiEulerEstimator():

    #derivatives = { 'a': da_dt, 'b': db_dt, ... }
    def __init__(self, derivatives):
        self.derivatives = derivatives

    #point = (t, {a: a(t), b: b(t), ... })
    def estimate_points(self, initial_point, step_size, num_steps):
        points = [ initial_point ]
        current_point = initial_point
        while num_steps > 0:
            num_steps -= 1
            derivatives_at_point = self._eval_derivative_at_point(current_point)
            deltas = dict((k, d * step_size) for (k, d) in derivatives_at_point.items())
            current_point = (current_point[0] + step_size, dict((k, delta + current_point[1][k]) for (k, delta) in deltas.items()))
            points.append(current_point)
        return points
    
    def _eval_derivative_at_point(self, point):
        result = {}
        for f_deriv in self.derivatives:
            result[f_deriv] = self.derivatives[f_deriv](point)
        return result

if __name__ == "__main__":
    initial_point = (-0.4, {"a": -0.45 , "b": -0.05 , "c": 0})

    def da_dt(point):
        return point[1]["a"] + 1
    
    def db_dt (point):
        return point[1]["a"] + point[1]["b"]
    
    def dc_dt (point):
        return 2*point[1]["b"] + 3*point[0]
    
    derivatives = { "a": da_dt, "b": db_dt, "c": dc_dt }

    euler = MultiEulerEstimator(derivatives)
    points = euler.estimate_points(initial_point, 2, 3)
    
    for point in points:
        print(point)