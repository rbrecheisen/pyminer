__author__ = 'Ralph'

import wx

from Node import NodeView
from NodeCanvasMenu import NodeCanvasMenu
from NodeMenu import NodeMenu


class NodeCanvas(wx.Panel):

    def __init__(self, parent):
        """
        Constructor for this canvas.
        :param parent: Parent widget
        :return:
        """
        super(NodeCanvas, self).__init__(parent)

        self.Bind(wx.EVT_PAINT, self._on_paint)
        self.Bind(wx.EVT_RIGHT_UP, self._on_right_click)
        self._nodes = []

    def create_node(self):
        """
        Creates new node symbol on the canvas
        :return:
        """
        position = self.ScreenToClient(wx.GetMousePosition())
        self._nodes.append(NodeView(position))
        self.Refresh()

    def delete_node(self, node):
        """
        Deletes given node
        :return:
        """
        self._nodes.remove(node)
        self.Refresh()

    # Event handlers

    def _on_paint(self, e):
        """
        Paints network nodes.
        :param e: Paint event
        :return:
        """
        device = wx.PaintDC(self)

        for node in self._nodes:
            node.render(device)

    def _on_right_click(self, e):
        """
        Called when user right-clicks on canvas
        :param e:
        :return:
        """
        position = e.GetPosition()
        menu = NodeCanvasMenu(self)
        for node in self._nodes:
            if node.contains(position):
                menu = NodeMenu(self, node)
                break
        self.PopupMenu(menu, e.GetPosition())