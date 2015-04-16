__author__ = 'Ralph'

import wx


class NodeCanvas(wx.Panel):

    def __init__(self, parent):
        """
        Constructor for this canvas.
        :param parent: Parent widget
        :return:
        """
        super(NodeCanvas, self).__init__(parent)
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def on_paint(self, e):
        """
        Paints network nodes.
        :param e: Paint event
        :return:
        """
        device = wx.PaintDC(self)
        device.DrawRectangle(100, 100, 300, 150)