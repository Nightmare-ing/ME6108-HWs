import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

WINDOW_WIDTH = 80
WINDOW_HEIGHT = 60
MARGIN = 15
RADIUS = 6


def main():
    rec_start = (MARGIN, MARGIN)
    rec_width = float(WINDOW_WIDTH - 2 * MARGIN)
    rec_height = float(WINDOW_HEIGHT - 2 * MARGIN)
    rhombus_vertices = generate_rhombus((rec_start[0], rec_start[1] +
                                        rec_height / 2.0), (rec_start[0] +
                                        rec_width / 2.0, rec_start[1] + rec_height))
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(0, WINDOW_WIDTH)
    ax.set_ylim(0, WINDOW_HEIGHT)
    ax.add_patch(mpatches.Rectangle(rec_start, rec_width, rec_height, fc='none',
                                    edgecolor='blue',
                                    linewidth=1, linestyle='--'))
    ax.add_patch(mpatches.Polygon(rhombus_vertices, closed=True,
                                  edgecolor='blue', fc='none'))
    plt.show()


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
    :return: list of discrete trace points
    """
    

if __name__ == '__main__':
    main()