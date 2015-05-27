__author__ = 'Ralph'

import wx

from canvas import Canvas

from network.importers import ImportCSV
from network.importers import ImportARFF
from network.selectors import SelectAttributes
from network.classifiers import SupportVectorMachine

from widgets import ImportCSVWidget
from widgets import ImportARFFWidget
from widgets import SelectAttributesWidget
from widgets import SupportVectorMachineWidget


class Application(wx.App):

    def __init__(self):

        super(Application, self).__init__()

        self._widgets = self._get_widgets()
        self._window = ApplicationWindow('PyMiner v1.0', self._widgets)

    def run(self):

        self._window.Show()
        self._window.SetSize((800, 500))
        self.MainLoop()

    @staticmethod
    def _get_widgets():

        widgets = list()
        widgets.append(ImportCSVWidget(ImportCSV()))
        widgets.append(ImportARFFWidget(ImportARFF()))
        widgets.append(SelectAttributesWidget(SelectAttributes()))
        widgets.append(SupportVectorMachineWidget(SupportVectorMachine()))

        return widgets


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
