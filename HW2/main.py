import os

import matplotlib.pyplot as plt

from HW2.drawer import Drawer
from utils import read_csv


def main():
    print("This is the demo of my HW2, there are some sample files under "
          "HW2/data, you can use them to test the program.")
    print("Or you can put your own data file under HW2/data and test it.")
    file = input("Please choose the data file you want to test(data1.csv or "
          "data2.csv): ")

    file_path = os.path.join(os.getcwd(), 'data', file)
    if not os.path.exists(file_path):
        print("The file does not exist, please try again.")
        main()
    print("You choose to test the file: ", file)
    drawer = Drawer()
    coors = read_csv(file_path, 3)
    which_view = input("Which view do you want to draw? (1 for Three View or 2 for Isometric View): ")
    if which_view == '1':
        print("Draw three view figure...")
        drawer.draw_three_view_fig(coors)
    elif which_view == '2':
        print("Draw isometric view figure...")
        drawer.draw_isometric_fig(coors)
    else:
        print("Invalid input, please try again.")
        main()
    plt.show()


if __name__ == '__main__':
    main()


