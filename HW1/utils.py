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

