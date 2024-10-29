import matplotlib.pyplot as plt


class Drawer:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        # invert the x axis
        self.fig.gca().invert_xaxis()

    def draw_connected_points(self, coordinates):
        """
        Draw connected points with given coordinates
        :param coordinates: np.array, [[x1, y1], [x2, y2], ...]
        """
        self.ax.plot(coordinates[:, 0], coordinates[:, 1])
