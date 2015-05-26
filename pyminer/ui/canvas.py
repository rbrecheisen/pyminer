__author__ = 'Ralph'

import wx


class Canvas(wx.Panel):

    def __init__(self, parent, widgets):

        super(Canvas, self).__init__(parent)
        self._widgets = widgets
        self._nodes = []

        self.Bind(wx.EVT_PAINT, self._render)
        self.Bind(wx.EVT_RIGHT_UP, self._show_menu)
        self.Bind(wx.EVT_LEFT_DOWN, self._start_dragging)
        self.Bind(wx.EVT_LEFT_UP, self._stop_dragging)
        self.Bind(wx.EVT_MOTION, self._move)
        self.Bind(wx.EVT_LEFT_DCLICK, self._show_dialog)

    def create_node(self):
        pass

    def delete_node(self):
        pass

    def _render(self, e):

        device = wx.PaintDC(self)
        for node in self._nodes:
            node.render(device)

    def _show_menu(self, e):

        position = e.GetPosition()

    def _start_dragging(self, e):
        pass

    def _stop_dragging(self, e):
        pass

    def _move(self, e):
        # either drag node around or a connection
        pass

    def _show_dialog(self):
        pass


class CanvasMenu(object):

    def __init__(self):

        super(CanvasMenu, self).__init__()


class Node(object):

    def __init__(self):

        super(Node, self).__init__()

    def render(self):
        pass


class NodeMenu(object):

    def __init__(self):

        super(NodeMenu, self).__init__()


class Connection(object):

    def __init__(self):

        super(Connection, self).__init__()


class ConnectionMenu(object):

    def __init__(self):

        super(ConnectionMenu, self).__init__()