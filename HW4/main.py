import matplotlib.pyplot as plt
import matplotlib.animation as animation

from HW4.bezier_curve import BezierCurve
from utils import read_data_prompt, read_coor


def main():
    file_path = read_data_prompt("HW4")
    coors = read_coor(file_path, 2)

    curve = BezierCurve(coors)
    fig, ax = plt.subplots()
    ani = animation.FuncAnimation(fig, curve.update, frames=curve.time_splits, init_func=curve.initialize_artists)
    plt.show()


if __name__ == '__main__':
    main()
