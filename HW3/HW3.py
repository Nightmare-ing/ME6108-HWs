import numpy as np
import matplotlib.pyplot as plt

max_iter = 800
grid_size = 1000
xlim = [-2.0, 1.0]
ylim = [-1.5, 1.5]

x = np.linspace(xlim[0], xlim[1], grid_size)
y = np.linspace(ylim[0], ylim[1], grid_size)
grid_x, grid_y = np.meshgrid(x, y)
mandelbrot_set = grid_x + 1j * grid_y
c = np.copy(mandelbrot_set)
iter_count = np.ones(mandelbrot_set.shape)

iterFunc = lambda z: z * z + c

for i in range(0, max_iter):
    mandelbrot_set = iterFunc(mandelbrot_set)
    iter_count += np.abs(mandelbrot_set) <= 2

color = np.log(iter_count)

plt.figure(figsize=(10, 10))
fig, ax = plt.subplots()
ax.scatter(grid_x, grid_y, c=color, cmap='viridis')

plt.show()
