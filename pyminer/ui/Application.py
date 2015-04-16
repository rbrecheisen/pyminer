__author__ = 'Ralph'

from ApplicationWindow import ApplicationWindow

import wx


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
        self.MainLoop()