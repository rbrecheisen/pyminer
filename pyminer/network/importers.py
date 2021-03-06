__author__ = 'Ralph'

import pandas as pd

from arff_utils import ARFF

from base import Node
from base import OutputPort


class Importer(Node):

    def __init__(self, name):

        super(Importer, self).__init__(name)


class ImportARFF(Importer):

    def __init__(self):

        super(ImportARFF, self).__init__('ImportARFF')
        self.add_output_port(OutputPort(name='output', data_type=pd.DataFrame))

        self.get_config().set('file_name', None)

    def execute(self):

        file_name = self.get_config().get('file_name')
        if file_name is None:
            raise RuntimeError('File name is empty')

        data = ARFF.read(file_name)
        data = ARFF.to_data_frame(data)

        self.get_output_port('output').set_data(data)


class ImportCSV(Importer):

    def __init__(self):

        super(ImportCSV, self).__init__('ImportCSV')
        self.add_output_port(OutputPort(name='output', data_type=pd.DataFrame))

        self.get_config().set('file_name', None)

    def execute(self):

        file_name = self.get_config().get('file_name')
        if file_name is None:
            raise RuntimeError('File name is empty')

        data = pd.read_csv(file_name, skipinitialspace=True)

        self.get_output_port('output').set_data(data)