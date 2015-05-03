__author__ = 'Ralph'

import os

import pandas as pd

from base import Node
from base import InputPort
from base import OutputPort


class ImportNode(Node):

    def __init__(self, name):
        super(ImportNode, self).__init__(name)


class ExportNode(Node):

    def __init__(self, name):
        super(ExportNode, self).__init__(name)


class ImportCSVNode(ImportNode):

    def __init__(self):
        super(ImportCSVNode, self).__init__('ImportCSV')
        self.add_output_port(
            OutputPort(name='output', data_type=pd.DataFrame))
        self.set_required_config_items(['file_name'])

    def execute(self):
        self.check_config()
        file_name = self.get_config().get('file_name')
        if not os.path.isfile(file_name):
            raise RuntimeError('File ' + file_name + ' does not exist')
        data = pd.read_csv(file_name)
        self.get_output_port('output').set_data(data)


class ExportCSVNode(ExportNode):

    def __init__(self):
        super(ExportCSVNode, self).__init__('ExportCSV')
        self.add_input_port(InputPort(name='input', data_type=pd.DataFrame))
        self.set_required_config_items(['file_name'])

    def execute(self):
        self.check_config()
        file_name = self.get_config().get('file_name')
        data = self.get_input_port('input').get_data()
        if data is not None:
            data.to_csv(file_name, index=False)