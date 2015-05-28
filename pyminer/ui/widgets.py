__author__ = 'Ralph'

import wx

from network.importers import ImportCSV
from network.importers import ImportARFF
from network.selectors import SelectAttributes
from network.classifiers import ApplyModel
from network.classifiers import SupportVectorMachine


class Widget(wx.Dialog):

    def __init__(self, node, name):

        super(Widget, self).__init__(None)

        self._node = node
        self._name = name

    def show(self):

        self.Show()

    def get_node(self):

        return self._node

    def get_name(self):

        return self._name


class WidgetItem(wx.BoxSizer):

    def __init__(self, parent, label):

        super(WidgetItem, self).__init__(wx.HORIZONTAL)
        self._label = wx.StaticText(parent, label=label)

    def get_label(self):
        return self._label

    def get_field(self):
        raise RuntimeError('Not implemented')


class FileWidgetItem(WidgetItem):

    def __init__(self, parent, label):

        super(FileWidgetItem, self).__init__(parent, label)

        self._field = wx.TextCtrl(parent)
        self._button = wx.Button(parent, label='Browse...')

        self.Add(self._label, proportion=0)
        self.Add(self._field, proportion=1)
        self.Add(self._button, proportion=0)

    def get_field(self):
        return self._field


class TextWidgetItem(WidgetItem):

    def __init__(self, parent, label):
        super(TextWidgetItem, self).__init__(parent, label)
        self._field = wx.TextCtrl(parent)
        self.Add(self._label, proportion=0)
        self.Add(self._field, proportion=1)

    def get_field(self):
        return self._field

class ChoiceWidgetItem(WidgetItem):

    def __init__(self, parent, label):
        super(ChoiceWidgetItem, self).__init__(parent, label)


class CheckWidgetItem(WidgetItem):

    def __init__(self, parent, label):
        super(CheckWidgetItem, self).__init__(parent, label)


class ImportCSVWidget(Widget):

    def __init__(self, node):

        super(ImportCSVWidget, self).__init__(node, 'ImportCSV')
        if not isinstance(self.get_node(), ImportCSV):
            raise RuntimeError('Node is not of type ImportCSV')

        config = self.get_node().get_config()
        self._layout = wx.FlexGridSizer(1, 2, 5, 10)


class ImportARFFWidget(Widget):

    def __init__(self, node):

        super(ImportARFFWidget, self).__init__(node, 'ImportARFF')
        if not isinstance(self.get_node(), ImportARFF):
            raise RuntimeError('Node is not of type ImportARFF')


class SelectAttributesWidget(Widget):

    def __init__(self, node):

        super(SelectAttributesWidget, self).__init__(node, 'SelectAttributes')
        if not isinstance(self.get_node(), SelectAttributes):
            raise RuntimeError('Node is not of type SelectAttributes')


class SupportVectorMachineWidget(Widget):

    def __init__(self, node):

        super(SupportVectorMachineWidget, self).__init__(node, 'SupportVectorMachine')
        if not isinstance(self.get_node(), SupportVectorMachine):
            raise RuntimeError('Node is not of type SupportVectorMachine')


class ApplyModelWidget(Widget):

    def __init__(self, node):

        super(ApplyModelWidget, self).__init__(node, 'ApplyModel')
        if not isinstance(self.get_node(), ApplyModel):
            raise RuntimeError('Node is not of type ApplyModel')