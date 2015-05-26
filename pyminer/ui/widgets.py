__author__ = 'Ralph'

from ..network.importers import ImportCSV
from ..network.importers import ImportARFF
from ..network.selectors import SelectAttributes
from ..network.classifiers import ApplyModel
from ..network.classifiers import SupportVectorMachine


class Widget(object):

    def __init__(self, node):

        super(Widget, self).__init__()
        self._node = node

    def get_node(self):

        return self._node


class ImportCSVWidget(Widget):

    def __init__(self, node):

        super(ImportCSVWidget, self).__init__(node)
        if not isinstance(self.get_node(), ImportCSV):
            raise RuntimeError('Node is not of type ImportCSV')


class ImportARFFWidget(Widget):

    def __init__(self, node):

        super(ImportARFFWidget, self).__init__(node)
        if not isinstance(self.get_node(), ImportARFF):
            raise RuntimeError('Node is not of type ImportARFF')


class SelectAttributesWidget(Widget):

    def __init__(self, node):

        super(SelectAttributesWidget, self).__init__(node)
        if not isinstance(self.get_node(), SelectAttributes):
            raise RuntimeError('Node is not of type SelectAttributes')


class SupportVectorMachineWidget(Widget):

    def __init__(self, node):

        super(SupportVectorMachineWidget, self).__init__(node)
        if not isinstance(self.get_node(), SupportVectorMachine):
            raise RuntimeError('Node is not of type SupportVectorMachine')


class ApplyModelWidget(Widget):

    def __init__(self, node):

        super(ApplyModelWidget, self).__init__(node)
        if not isinstance(self.get_node(), ApplyModel):
            raise RuntimeError('Node is not of type ApplyModel')