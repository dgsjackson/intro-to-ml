import numpy as np
from matplotlib import pyplot

x = np.linspace(-5, 10, 100)

fig, axes_arr = pyplot.subplots(2,2)

graph1 = axes_arr[0,0]
graph1.plot(x, 1.357*x - 2.2857)
graph1.scatter([1, 3, 4], [0, -1, 5])

graph2 = axes_arr[0,1]
graph2.plot(x, 0.0238095*x + 1.71429)
graph2.scatter([-2, 1, 3, 4], [3, 0, -1, 5])

graph3 = axes_arr[1,0]
graph3.plot(x, 0.5227*x**2 - 0.947*x - 0.75)
graph3.scatter([-2, 1, 3, 4], [3, 0, -1, 5])

graph4 = axes_arr[1,1]
graph4.plot(x, 0.35*x**3 - 0.6*x**2 - 2.64*x + 2.9)
graph4.scatter([-3, -2, 3, 1, 4], [-4, 3, -1, 0, 5])

fig2 = pyplot.figure()

graph5 = fig2.add_subplot(projection='3d')
y = np.linspace(-5, 10, 100)
XX, YY = np.meshgrid(x, y)
ZZ = 1.087*XX + 0.306*YY - 2.667
graph5.plot_surface(XX, YY, ZZ, alpha=0.2)
graph5.scatter([-2, 1, 3, 4], [3, 0, -1, 5], [-3, -4, 2, 3])

pyplot.show()