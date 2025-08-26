import matplotlib.pyplot as plt

class EulerEstimator():

    def __init__(self, deriv):
        self.deriv = deriv

    def estimate_points(self, initial_point, step_size, num_steps):
        points = [ initial_point ]
        current_point = initial_point
        while num_steps > 0:
            num_steps -= 1
            deriv = self.deriv(current_point)
            delta_y = deriv * step_size
            current_point = (current_point[0] + step_size, current_point[1] + delta_y)
            points.append(current_point)
        return points
    
if __name__ == "__main__":
    f_deriv = lambda p: 2*p[0]
    euler = EulerEstimator(f_deriv)

    initial_points = [(0, -2), (0, -1), (0, 0), (0, 1), (0, 2)]
    for point in initial_points:
        points = euler.estimate_points(point, 0.25, 20)
        x = list(map(lambda p: p[0], points))
        y = list(map(lambda p: p[1], points))
        plt.plot(x, y)
    
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()