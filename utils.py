import csv
import os.path

import numpy as np


def generate_rhombus(point1, point2):
    """
    Generate all four vertices according to the given points.
    :param point1: coordinates of the left most point
    :param point2: coordinates of the highest point
    :return: list of all four vertices
    """
    point3 = (2 * point2[0] - point1[0], point1[1])
    point4 = (point2[0], 2 * point1[1] - point2[1])
    return [point1, point2, point3, point4]


def generate_trace(rhombus_vertices):
    """
    generate discrete trace points for the given rhombus.
    :param rhombus_vertices: coordinates of the vertices of the rhombus
    :return: two numpy array of the coordinates of the discrete trace points, x, y
    """
    left_up_x = np.linspace(rhombus_vertices[0][0], rhombus_vertices[1][0], 100)
    left_up_y = np.linspace(rhombus_vertices[0][1], rhombus_vertices[1][1], 100)
    right_up_x = np.linspace(rhombus_vertices[1][0], rhombus_vertices[2][0], 100)
    right_up_y = np.linspace(rhombus_vertices[1][1], rhombus_vertices[2][1], 100)
    right_down_x = np.linspace(rhombus_vertices[2][0], rhombus_vertices[3][0], 100)
    right_down_y = np.linspace(rhombus_vertices[2][1], rhombus_vertices[3][1], 100)
    left_down_x = np.linspace(rhombus_vertices[3][0], rhombus_vertices[0][0], 100)
    left_down_y = np.linspace(rhombus_vertices[3][1], rhombus_vertices[0][1], 100)
    return np.concatenate((left_up_x, right_up_x, right_down_x, left_down_x)), np.concatenate(
        (left_up_y, right_up_y, right_down_y, left_down_y))


def read_homogeneous_coor(file_path, data_per_row):
    """
    Read the csv file and return the homogeneous coordinates data as a
    numpy array
    :param file_path: the path of the csv file
    :param data_per_row: number of data in each row
    :return: the data in the csv file, in the form of numpy array
    """
    coors = read_coor(file_path, data_per_row)
    return np.hstack((coors, np.ones((coors.shape[0], 1))))

def read_coor(file_path, data_per_row):
    """
    Read the csv file and return the 2d coordinates data as a numpy array
    :param file_path: the path of the csv file
    :param data_per_row: number of data in each row
    :return: the data in the csv file, in the form of numpy array
    """
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        coors = []
        for row in reader:
            if len(row) != data_per_row:
                raise ValueError('Invalid data format')
            coors.append([float(i) for i in row])
        coors = np.array(coors)
    return coors

def read_data_prompt(hw):
    """
    Prompt when reading a test data file
    :param hw: String for HWs, for example "HW1", "HW2", ...
    :return: path of the file
    """
    print("This is the demo of my {}, there are some sample files under "
          "{}/data, you can use them to test the program".format(hw, hw))
    print("Or you can put your own data file under {}/data and test "
          "them.".format(hw))

    while True:
        file = input("Please choose the data file you want to test(data1.csv or "
                     "data2.csv): ")
        file_path = os.path.join(os.getcwd(), hw, 'data', file)
        if not os.path.exists(file_path):
            print("The file does not exist, please try again.")
        else:
            break

    print("You choose to test the file: ", file)
    return file_path

