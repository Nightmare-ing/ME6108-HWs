import numpy as np


def trivs(coordinates, dist_of_view, which_view, theta, fi):
    """
    Calculate the transformed coordinates of three views and isometric drawing
    for the given input points.
    :param coordinates: the input points, in the form of np.array, [[x1, y1, z1], [x2, y2, z2], ...]
    :param dist_of_view: Distance between each view
    :param which_view: the view to be transformed, 'front profile', 'top profile', 'side profile', 'isometric'
    :param theta: the angle of rotation around z-axis
    :param fi: the angle of rotation around x-axis
    :return: coordinates of transformed points in the specified view,
    in the form of np.arrays [[x1, y1], [x2, y2], ...]
    """
    trans_coor = np.dot(coordinates, get_trans_matrix(dist_of_view,
                                                      which_view,
                                                      theta, fi))
    x_col = trans_coor[:, 0].reshape(-1, 1)
    z_col = trans_coor[:, 2].reshape(-1, 1)
    return np.concatenate((x_col, z_col), axis=1)


def get_trans_matrix(dist_of_view, which_view, theta, fi):
    """
    Get the transformation matrix for the given view and rotation angles.
    :param dist_of_view: Distance between each view
    :param which_view: the view to be transformed, 'front profile', 'top profile', 'side profile', 'isometric'
    :param theta: the angle of rotation around z-axis, in radians
    :param fi: the angle of rotation around x-axis, in radians
    :return: the transformation matrix
    """
    if which_view == 'front profile':
        return np.array([[1, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 1]])
    elif which_view == 'top profile':
        return np.array([[1, 0, 0, 0],
                         [0, 0, -1, 0],
                         [0, 0, 0, 0],
                         [0, 0, -dist_of_view, 1]])
    elif which_view == 'side profile':
        return np.array([[0, 0, 0, 0],
                         [-1, 0, 0, 0],
                         [0, 0, 1, 0],
                         [-dist_of_view, 0, 0, 1]])
    elif which_view == 'isometric':
        return np.array([[np.cos(theta), 0, -np.sin(theta) * np.sin(fi), 0],
                         [-np.sin(theta), 0, -np.cos(theta) * np.sin(fi), 0],
                         [0, 0, np.cos(fi), 0],
                         [0, 0, 0, 1]])
    else:
        raise ValueError('Invalid view name')
