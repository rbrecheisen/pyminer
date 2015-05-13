__author__ = 'Ralph'

import wx

from NodeCanvas import NodeCanvas


class ApplicationWindow(wx.Frame):

    def __init__(self, title):
        """
        Constructor for this application window.
        :param title: Window title
        :return:
        """
        super(ApplicationWindow, self).__init__(None, -1, title)
        self._canvas = NodeCanvas(self)