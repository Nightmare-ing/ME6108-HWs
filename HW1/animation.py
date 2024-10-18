import math

import matplotlib.animation as animation
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from HW1.utils import generate_rhombus, generate_trace


def update(frame):
    """
    For updating each frame of the animation
    :param frame: represent which frame
    :return: updated Artiest objects
    """
    global ball
    ball.set_center((trace_x[frame % trace_x.size],
                     trace_y[frame % trace_y.size]))


def press(event):
    """
    For handling key press event
    :param event:  object transferred in
    :return: None
    """
    global animation_paused
    if event.key is not None:
        if animation_paused:
            ani.event_source.start()
        else:
            ani.event_source.stop()
        animation_paused = not animation_paused


# Set some parameters for the animation
WINDOW_WIDTH = 200
WINDOW_HEIGHT = 150
MARGIN = 15
RADIUS = 6

# Compute some parameters for the animation
animation_paused = False
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

# Draw the rectangle and the rhombus
ax.add_patch(mpatches.Rectangle(rec_start, rec_width, rec_height, fc='none',
                                edgecolor='blue',
                                linewidth=1, linestyle='--'))
ax.add_patch(mpatches.Polygon(edge_rhombus, closed=True,
                              edgecolor='blue', fc='none'))

# Compute the trace of the ball and draw the ball
theta = math.atan((edge_rhombus[1][1] - edge_rhombus[0][1]) / (edge_rhombus[1][0] - edge_rhombus[0][0]))
trace_rhombus = generate_rhombus((edge_rhombus[0][0] + RADIUS / math.sin(theta), edge_rhombus[0][1]),
                                 (edge_rhombus[1][0], edge_rhombus[1][1] - RADIUS / math.cos(theta)))
trace_x, trace_y = generate_trace(trace_rhombus)
ball = ax.add_patch(mpatches.Circle((trace_x[0], trace_y[0]), RADIUS,
                                    color='red',
                                    fc='none'))

# Connect the key press event and start the animation
fig.canvas.mpl_connect('key_press_event', press)
ani = animation.FuncAnimation(fig, update, frames=trace_x.size, interval=10, repeat=True)
plt.show()
