import os.path
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from HW5.b_spline import BSpline
from utils import read_coor


def main():
    file_path = os.path.join(os.getcwd(), 'HW5/data/data1.csv')
    coors = read_coor(file_path, 2)

    fig, ax = plt.subplots()
    ax.set_xlim(np.min(coors[:, 0]) - 0.5, np.max(coors[:, 0]) + 0.5)
    ax.set_ylim(np.min(coors[:, 1]) - 0.5, np.max(coors[:, 1]) + 0.5)
    curve = BSpline(ax, coors, 100)
    ani = animation.FuncAnimation(fig, curve.update,
                                    frames=curve.time_splits,
                                    init_func=curve.initialize_artists,
                                  interval=100, blit=True)
    plt.show()

if __name__ == '__main__':
    main()
    