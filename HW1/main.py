import subprocess

import matplotlib.pyplot as plt

from HW1.scanning_algorithms import bresenham_line_standard, bresenham_circle
from HW1.ui import ScanningDrawer, get_input_line, get_input_circle, AnimationDrawer


def main():
    print("This is the demo of my HW1, do you want to check problem 1 or problem 2?")
    problem = input("Please input 1 for problem 1 or 2 for problem 2: ")
    if problem == '1':
        drawer = ScanningDrawer()
        print("You choose problem 1...")
        print("!!!ATTENTION!!!: if you want to show line, only support line "
              "with "
              "positive slope")
        line_or_circle = input("Do you want to draw a line or a circle? "
                               "Enter 1 for line, 2 for circle: ")
        subdivision = input("If you want to set subdivision to see the "
                            "effect of line scanning, please input "
                            "the number of subdivisions(default is 1000). "
                            "If you don't, just press the ENTER: ")
        if line_or_circle == '1':
            start, end = get_input_line()
            if subdivision:
                x, y = bresenham_line_standard(start, end, int(subdivision))
            else:
                x, y = bresenham_line_standard(start, end)

            # Set the figure size
            xlim_left = min(start[0], end[0]) - 5
            xlim_right = max(start[0], end[0]) + 5
            ylim_down = min(start[1], end[1]) - 5
            ylim_up = max(start[1], end[1]) + 5
            drawer.set_fig((xlim_left, xlim_right), (ylim_down, ylim_up))

            drawer.line_drawer(x, y)
        elif line_or_circle == '2':
            print("You choose to draw a circle...")
            center, radius = get_input_circle()
            if subdivision:
                x, y = bresenham_circle(center, int(radius), int(subdivision))
            else:
                x, y = bresenham_circle(center, int(radius))
            drawer.set_fig((center[0] - int(radius) - 5, center[0] + int(radius) + 5),
                           (center[1] - int(radius) - 5, center[1] + int(radius) + 5))
            drawer.circle_drawer(x, y, center, int(radius))
        plt.show()
    elif problem == '2':
        animation_drawer = AnimationDrawer()
        print("You choose problem 2, run the animation")
        animation_drawer.set_fig()
        animation_drawer.show_animation()
        plt.show()
    else:
        print("Invalid input, please try again.")
        main()


if __name__ == '__main__':
    main()
