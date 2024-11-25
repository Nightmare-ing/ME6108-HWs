import os

import matplotlib.pyplot as plt

from HW2.drawer import Drawer
from utils import read_csv, read_data_prompt


def main():
    file_path = read_data_prompt("HW2")
    drawer = Drawer()
    coors = read_csv(file_path, 3)

    while True:
        which_view = input("Which view do you want to draw? (1 for Three View or 2 for Isometric View): ")
        if which_view == '1':
            print("Draw three view figure...")
            drawer.draw_three_view_fig(coors)
            break
        elif which_view == '2':
            print("Draw isometric view figure...")
            drawer.draw_isometric_fig(coors)
            break
        else:
            print("Invalid input, please try again.")
    plt.show()


if __name__ == '__main__':
    main()


