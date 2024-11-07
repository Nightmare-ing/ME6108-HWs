import numpy as np
import matplotlib.pyplot as plt

z0 = 1 + 1j
c = 1j
iter_count = 800
mandelbrot_set = np.zeros(iter_count)
mandelbrot_set[0] = z0

iterFunc = lambda x: x * x + c

for i in range(1, iter_count):
    mandelbrot_set[i] = iterFunc(mandelbrot_set[i - 1])

fig, ax = plt.subplots()
ax.plot(mandelbrot_set.real, mandelbrot_set.imag)

plt.show()
