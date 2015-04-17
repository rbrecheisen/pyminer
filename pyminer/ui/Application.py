__author__ = 'Ralph'

import wx

from ApplicationWindow import ApplicationWindow


class Application(wx.App):

    def __init__(self):
        """
        Constructor for this application
        :return:
        """
        super(Application, self).__init__()
        self._window = ApplicationWindow(title='PyMiner')

    def run(self):
        """
        Runs the application by showing the main window.
        :return:
        """
        self._window.Show()
        self._window.Maximize(True)

        self.MainLoop()