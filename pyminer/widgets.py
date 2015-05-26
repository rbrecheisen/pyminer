__author__ = 'Ralph'

import wx

from pyminer.network.importers import ImportCSVNode
from exporters import ExportCSVNode
from filters import FilterAttributesNode


class Widget(wx.Dialog):

    def __init__(self, title):

        super(Widget, self).__init__(None, -1, title)

    def get_node(self):
        raise RuntimeError('Not implemented')

    def show(self):

        self.Show()

    def close(self):

        self.Show(False)


class ImportCSVWidget(Widget):

    def __init__(self):

        super(ImportCSVWidget, self).__init__('ImportCSV')

        self._node = ImportCSVNode()
        self._node.get_config().set('file_name', '')

        panel = wx.Panel(self, -1)

        button = wx.Button(panel, label='Ok')
        self.Bind(wx.EVT_BUTTON, self._save_config)

        self._text_field = wx.TextCtrl(panel)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(wx.StaticText(panel, label='File name:'))
        sizer.Add(self._text_field)
        sizer.Add(button)
        panel.SetSizer(sizer)

        self.SetSize((300, 100))

    def get_node(self):

        return self._node

    def get_name(self):

        return self._node.get_name()

    def _save_config(self, event):

        file_name = self._text_field.GetValue()
        self.get_node().get_config().set('file_name', file_name)
        self.close()


class ExportCSVWidget(Widget):

    def __init__(self):

        super(ExportCSVWidget, self).__init__('ExportCSV')

        self._node = ExportCSVNode()
        self._node.get_config().set('file_name', '')

        panel = wx.Panel(self, -1)
        button = wx.Button(panel, label='Ok')
        self.Bind(wx.EVT_BUTTON, self._save_config)
        self._text_field = wx.TextCtrl(panel)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(wx.StaticText(panel, label='File name:'))
        sizer.Add(self._text_field)
        sizer.Add(button)
        panel.SetSizer(sizer)

        self.SetSize((300, 100))

    def get_node(self):

        return self._node

    def get_name(self):

        return self._node.get_name()

    def _save_config(self, event):

        file_name = self._text_field.GetValue()
        self.get_node().get_config().set('file_name', file_name)
        self.close()


class FilterAttributesWidget(Widget):

    def __init__(self):

        super(FilterAttributesWidget, self).__init__('FilterAttributes')

        self._node = FilterAttributesNode()
        self._node.get_config().set('filter_type', 'all')
        self._node.get_config().set('invert_filter', True)