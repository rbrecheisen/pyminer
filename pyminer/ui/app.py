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


class Example(wx.Frame):

    def __init__(self, parent, title):

        super(Example, self).__init__(parent, title=title, size=(260, 180))
        self._setup_ui()
        self.Center()
        self.Show()

    def _setup_ui(self):

        panel = wx.Panel(self, -1)

        labels = list()
        labels.append(wx.StaticText(panel, label='selector_type'))
        labels.append(wx.StaticText(panel, label='attributes'))
        labels.append(wx.StaticText(panel, label='invert_filter'))

        fields = list()
        fields.append(wx.ComboBox(panel, choices=['all', 'single', 'subset']))
        fields.append(wx.TextCtrl(panel))
        fields.append(wx.CheckBox(panel))

        grid = wx.FlexGridSizer(3, 2, 5, 10)
        grid.AddMany([
            (labels[0]),
            (fields[0], 2, wx.EXPAND),
            (labels[1]),
            (fields[1], 2, wx.EXPAND),
            (labels[2]),
            (fields[2], 2, wx.EXPAND)
        ])

        grid.AddGrowableCol(1, 1)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(grid, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)

        panel.SetSizer(hbox)