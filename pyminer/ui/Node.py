__author__ = 'Ralph'


class NodeView(object):

    def __init__(self, position):
        """
        Constructor of this node symbol
        :return:
        """
        self._width  = 50
        self._height = 50
        self._position = (position[0] - self._width / 2, position[1] - self._height / 2)

    def contains(self, position):
        """
        Checks if given position lies inside node boundaries
        :param position: Position
        :return: True/False
        """
        x = position[0]
        y = position[1]
        if x > self.x() and x < self.x() + self.width() and y > self.y() and y < self.y() + self.height():
            return True
        return False

    def render(self, device):
        """
        Renders this node
        :return:
        """
        device.DrawRectangle(self.x(), self.y(), self.width(), self.height())

    def x(self):
        return self._position[0]

    def y(self):
        return self._position[1]

    def width(self):
        return self._width

    def height(self):
        return self._height