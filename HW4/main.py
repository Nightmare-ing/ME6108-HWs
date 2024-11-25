import matplotlib.pyplot as plt
import matplotlib.animation as animation

from HW4.bezier_curve import BezierCurve
from utils import read_data_prompt, read_coor


def main():
    file_path = read_data_prompt("HW4")
    coors = read_coor(file_path, 2)

    fig, ax = plt.subplots()
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(-0.5, 1.5)
    curve = BezierCurve(ax, coors)
    # for item in curve.initialize_artists():
    #     ax.add_line(item)
    ani = animation.FuncAnimation(fig, curve.update, frames=curve.time_splits, init_func=curve.initialize_artists, interval=100)
    plt.show()


if __name__ == '__main__':
    main()
