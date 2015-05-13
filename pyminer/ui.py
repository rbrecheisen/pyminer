__author__ = 'Ralph'

import wx


class Application(wx.App):

    def __init__(self):

        super(Application, self).__init__()
        self._window = ApplicationWindow('PyMiner v1.0')

    def run(self):

        self._window.Show()
        self._window.SetSize((500, 500))
        self.MainLoop()

class ApplicationWindow(wx.Frame):

    def __init__(self, title):

        super(ApplicationWindow, self).__init__(None, -1, title)
        self._canvas = NodeCanvas(self)


class Node(object):

    def __init__(self, position):

        super(Node, self).__init__()
        self._dragging = False
        self._width  = 50
        self._height = 50
        self._position = (0, 0)
        self.set_position(position)

    def is_dragging(self):

        return self._dragging

    def set_dragging(self, dragging):

        self._dragging = dragging

    def x(self):

        return self._position[0]

    def set_x(self, x):

        self._position = (x, self._position[1])
        return self._position

    def y(self):

        return self._position[1]

    def set_y(self, y):

        self._position = (self._position[0], y)

    def get_position(self):

        return self._position

    def set_position(self, position):

        self._position = (position[0] - self._width / 2, position[1] - self._height / 2)

    def width(self):

        return self._width

    def height(self):

        return self._height

    def contains(self, position):

        x = position[0]
        y = position[1]
        if self.x() < x < self.x() + self.width() and self.y() < y < self.y() + self.height():
            return True
        return False

    def render(self, device):

        device.DrawRectangle(self.x(), self.y(), self.width(), self.height())


class NodeCanvas(wx.Panel):

    def __init__(self, parent):

        super(NodeCanvas, self).__init__(parent)
        self.Bind(wx.EVT_PAINT, self._on_paint)
        self.Bind(wx.EVT_RIGHT_UP, self._on_right_click)
        self.Bind(wx.EVT_LEFT_DOWN, self._on_left_click_down)
        self.Bind(wx.EVT_LEFT_UP, self._on_left_click_up)
        self.Bind(wx.EVT_MOTION, self._on_mouse_move)
        self._nodes = []

    def create_node(self):

        position = self.ScreenToClient(wx.GetMousePosition())
        self._nodes.append(Node(position))
        self.Refresh()

    def delete_node(self, node):

        self._nodes.remove(node)
        self.Refresh()

    # EVENT HANDLERS

    def _on_paint(self, event):

        device = wx.PaintDC(self)
        for node in self._nodes:
            node.render(device)

    def _on_right_click(self, event):

        position = event.GetPosition()
        menu = NodeCanvasMenu(self)
        for node in self._nodes:
            if node.contains(position):
                menu = NodeMenu(self, node)
                break
        self.PopupMenu(menu, event.GetPosition())

    def _on_left_click_down(self, event):

        position = event.GetPosition()
        for node in self._nodes:
            node.set_dragging(False)
            if node.contains(position):
                node.set_dragging(True)
                break

    def _on_left_click_up(self, event):

        for node in self._nodes:
            node.set_dragging(False)

    def _on_mouse_move(self, event):

        # todo: calculate delta between mouse and node positions
        for node in self._nodes:
            if node.is_dragging():
                node.set_position(event.GetPosition())
        self.Refresh()


class NodeMenu(wx.Menu):

    def __init__(self, parent, node):

        super(NodeMenu, self).__init__()
        self._parent = parent
        self._node = node
        item = wx.MenuItem(self, wx.NewId(), 'Delete Node')
        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self._on_delete_node, item)

    # EVENT HANDLERS

    def _on_delete_node(self, event):

        self._parent.delete_node(self._node)


class NodeCanvasMenu(wx.Menu):

    def __init__(self, parent):

        super(NodeCanvasMenu, self).__init__()
        self._parent = parent
        item = wx.MenuItem(self, wx.NewId(), 'Create Node')
        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self._on_create_node, item)

    # EVENT HANDLERS

    def _on_create_node(self, event):

        self._parent.create_node()