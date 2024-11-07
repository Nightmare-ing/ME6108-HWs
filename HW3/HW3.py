import numpy as np
import matplotlib.pyplot as plt

max_iter = 800
grid_size = 1000
xrange = [-2.0, 1.0]
yrange = [-1.5, 1.5]
iterFunc = lambda z: z * z + c

x = np.linspace(xrange[0], xrange[1], grid_size)
y = np.linspace(yrange[0], yrange[1], grid_size)
grid_x, grid_y = np.meshgrid(x, y)
mandelbrot_set = grid_x + 1j * grid_y
c = np.copy(mandelbrot_set)
iter_count = np.ones(mandelbrot_set.shape)

for i in range(0, max_iter):
    mandelbrot_set = iterFunc(mandelbrot_set)
    iter_count += np.abs(mandelbrot_set) <= 2

color = np.log(iter_count)

plt.figure(figsize=(9, 9))
plt.scatter(grid_x, grid_y, c=color, cmap='viridis')

plt.show()
