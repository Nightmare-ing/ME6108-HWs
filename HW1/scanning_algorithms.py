import numpy as np

def bresenham_line_standard(start, end, subdivision):
    """
    Return a numpy array of discrete points generated by Bresenhan algorithm
    :param start: start point of the line
    :param end: end point of the line
    :param subdivision: number of divisions of the line
    :return: numpy, array of discrete points generated by Bresenhan algorithm
    """
    k = float(end[1] - start[1]) / float(end[0] - start[0])
    if k <= 1:
        unit = (end[0] - start[0]) / subdivision
        pixel_x, pixel_y = standard_helper(subdivision, start, k, unit)
    else:
        k = 1 / k
        unit = (end[1] - start[1]) / subdivision
        pixel_y, pixel_x = standard_helper(subdivision, (start[1],
                                                         start[0]), k,
                                           unit)
    return pixel_x, pixel_y


def bresenham_line_optimized(start, end, subdivision):
    """
    Optimized bresenham line algorithm with parallel computing technique
    :param start: start point of the line
    :param end: end point of the line
    :param subdivision: number of divisions of the line
    :return: numpy, array of discrete points generated by Bresenhan algorithm
    """
    k = float(end[1] - start[1]) / float(end[0] - start[0])
    if k == 1:
        pixel_x = np.arange(0, subdivision + 1) + start[0]
        pixel_y = np.arange(0, subdivision + 1) + start[1]
    elif k < 1:
        pixel_x, pixel_y = optimized_helper(subdivision, start, end, k)
    else:
        pixel_y, pixel_x = optimized_helper(subdivision, (start[1],
                                                          start[0]),
                                            (end[1], end[0]), 1/k)
    return pixel_x, pixel_y


def standard_helper(subdivision, start, k, unit):
    """
    Implement bresenham scanning algorithm when k <= 1
    :param subdivision: number of divisions of the line
    :param start: start point of the line
    :param k: slope of the line
    :param unit: step increment of x
    :return: scanned result pixel_x, pixel_y in numpy array form
    """
    pixel_x = np.zeros(subdivision + 1)
    pixel_y = np.zeros(subdivision + 1)
    x = start[0]
    y = start[1]
    e = -0.5
    for i in range(subdivision + 1):
        pixel_x[i] = x
        pixel_y[i] = y
        x = x + unit
        e = e + k
        if e >= 0:
            y = y + unit
            # when move up for one pixel, should also compare with another
            # 0.5, but now the position is "negative", so it's e - 1
            e = e - 1

    return pixel_x, pixel_y

def optimized_helper(subdivision, start, end, k):
    """
    Implement optimized bresenham scanning algorithm when k <= 1
    :param subdivision: number of divisions of the line
    :param start: start point of the line
    :param end: end point of the line
    :param k: slope of the line
    :return: scanned result pixel_x, pixel_y in numpy array form
    """
    pixel_x = np.linspace(start[0], end[0], subdivision + 1)
    d, _ = np.modf(np.arange(0, k * (subdivision + 1), k))
    unit = (end[0] - start[0]) / subdivision
    e = d - 0.5
    e = np.where(e >= 0, 1, 0) * unit
    pixel_y = np.cumsum(e) + start[1]
    return pixel_x, pixel_y