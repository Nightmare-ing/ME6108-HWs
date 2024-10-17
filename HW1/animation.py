import math

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from HW1.utils import generate_rhombus, generate_trace

WINDOW_WIDTH = 200
WINDOW_HEIGHT = 150
MARGIN = 15
RADIUS = 6

rec_start = (MARGIN, MARGIN)
rec_width = float(WINDOW_WIDTH - 2 * MARGIN)
rec_height = float(WINDOW_HEIGHT - 2 * MARGIN)
edge_rhombus = generate_rhombus((rec_start[0], rec_start[1] +
                                 rec_height / 2.0), (rec_start[0] +
                                                     rec_width / 2.0, rec_start[1] + rec_height))

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(0, WINDOW_WIDTH)
ax.set_ylim(0, WINDOW_HEIGHT)
ax.add_patch(mpatches.Rectangle(rec_start, rec_width, rec_height, fc='none',
                                edgecolor='blue',
                                linewidth=1, linestyle='--'))
ax.add_patch(mpatches.Polygon(edge_rhombus, closed=True,
                              edgecolor='blue', fc='none'))
theta = math.atan((edge_rhombus[1][1] - edge_rhombus[0][1]) / (edge_rhombus[1][0] - edge_rhombus[0][0]))
trace_rhombus = generate_rhombus((edge_rhombus[0][0] + RADIUS/math.sin(theta), edge_rhombus[0][1]),
                                 (edge_rhombus[1][0], edge_rhombus[1][1] - RADIUS/math.cos(theta)))
trace_x, trace_y = generate_trace(trace_rhombus)
ball = ax.add_patch(mpatches.Circle((trace_x[0], trace_y[0]), RADIUS,
                                    color='red',
                                    fc='none'))


def update(frame):
    """
    For updating each frame of the animation
    :param frame: represent which frame
    :return: updated Artiest objects
    """
    ball.set_center((trace_x[frame % trace_x.size],
                     trace_y[frame % trace_y.size]))



ani = animation.FuncAnimation(fig, update, interval=1, repeat=True)
plt.show()

