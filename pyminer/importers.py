__author__ = 'Ralph'

import os

import pandas as pd

from arff_utils import ARFF

from base import Node
from base import OutputPort


class Importer(Node):
    pass


class ImportNode(Node):

    def __init__(self, name):
        super(ImportNode, self).__init__(name)


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
        data = pd.read_csv(file_name, skipinitialspace=True)
        self.get_output_port('output').set_data(data)


class ImportARFFNode(ImportNode):

    def __init__(self):

        super(ImportARFFNode, self).__init__('ImportARFF')
        self.add_output_port(
            OutputPort(name='output', data_type=pd.DataFrame))
        self.set_required_config_items(['file_name'])

    def execute(self):

        self.check_config()
        file_name = self.get_config().get('file_name')
        if not os.path.isfile(file_name):
            raise RuntimeError('File ' + file_name + ' does not exist')
        data = ARFF.read(file_name)
        data = ARFF.to_data_frame(data)
        self.get_output_port('output').set_data(data)