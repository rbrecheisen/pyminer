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

    def get_node(self):

        return self._node

    def get_name(self):

        return self._name


class ImportCSVWidget(Widget):

    def __init__(self, node):

        super(ImportCSVWidget, self).__init__(node, 'ImportCSV')
        if not isinstance(self.get_node(), ImportCSV):
            raise RuntimeError('Node is not of type ImportCSV')


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