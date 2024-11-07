import numpy as np
import matplotlib.pyplot as plt

def normalize_color(data: np.ndarray, limit=256, apply_fun=lambda x: x):
    """ Normalize the input data to color range, the upper limit of the color value is set by `limit`
    :param data: data to be normalized
    :param limit: upper limit of the color value, default to be 256 RGB value
    :param apply_fun: first apply the desired function, then normalize the data, to avoid the situation that the data
    centered at some value in which case equally distribution is not very suitable
    :return: normalized color data
    """
    modified_data = apply_fun(data)
    max_value = modified_data.max()
    min_value = modified_data.min()
    return (modified_data - min_value) / max_value * limit


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

color = normalize_color(iter_count, 256, np.log)

plt.figure(figsize=(9, 9))
plt.scatter(grid_x, grid_y, c=color, cmap='viridis')

plt.show()
