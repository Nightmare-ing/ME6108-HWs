import os.path

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from HW4.bezier_curve import BezierCurve
from utils import read_data_prompt, read_coor


def main():
    file_path = read_data_prompt("HW4")
    coors = read_coor(file_path, 2)

    fig, ax = plt.subplots()
    ax.set_xlim(np.min(coors[:, 0]) - 0.5, np.max(coors[:, 0]) + 0.5)
    ax.set_ylim(np.min(coors[:, 1]) - 0.5, np.max(coors[:, 1]) + 0.5)
    curve = BezierCurve(ax, coors, 1000)
    ani = animation.FuncAnimation(fig, curve.update,
                                  frames=curve.time_splits,
                                  init_func=curve.initialize_artists, interval=10, blit=True)
    plt.show()


if __name__ == '__main__':
    main()
