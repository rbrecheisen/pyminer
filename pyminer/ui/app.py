__author__ = 'Ralph'

import wx

from canvas import Canvas


class Application(wx.App):

    def __init__(self):

        super(Application, self).__init__()

        self._widgets = []
        self._window = ApplicationWindow('PyMiner v1.0', self._widgets)

    def run(self):

        self._window.Show()
        self._window.SetSize((800, 500))
        self.MainLoop()


class ApplicationWindow(wx.Frame):

    def __init__(self, title, widgets):

        super(ApplicationWindow, self).__init__(None, -1, title)

        self._widgets = widgets
        self._canvas = Canvas(self, self._widgets)
        self.Bind(wx.EVT_CLOSE, self._close)

    def _close(self, e):

        for widget in self._widgets:
            widget.Destroy()
        self.Destroy()
