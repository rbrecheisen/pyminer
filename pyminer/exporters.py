__author__ = 'Ralph'

import pandas as pd

from arff_utils import ARFF

from base import Node
from base import InputPort

# TODO: update ARFF.from_data_frame() to automatically detect attributes and types


class Exporter(Node):
    """
    Exports Pandas data frame to various output formats.
    """
    def __init__(self, name):

        super(Exporter, self).__init__(name)

    def execute(self):

        raise RuntimeError('Not implemented')


class ExportARFF(Exporter):

    def __init__(self):

        super(ExportARFF, self).__init__('ExportARFF')
        self.add_input_port(InputPort(name='input', data_type=pd.DataFrame))
        self.set_required_config_items(['file_name'])

    def execute(self):

        self.check_config()
        file_name = self.get_config().get('file_name')
        data = self.get_input_port('input').get_data()
        if data is not None:
            ARFF.write(file_name, ARFF.from_data_frame('output', data))


class ExportCSV(Exporter):

    def __init__(self):

        super(ExportCSV, self).__init__('ExportCSV')
        self.add_input_port(InputPort(name='input', data_type=pd.DataFrame))
        self.set_required_config_items(['file_name'])

    def execute(self):

        self.check_config()
        file_name = self.get_config().get('file_name')
        data = self.get_input_port('input').get_data()
        if data is not None:
            data.to_csv(file_name, index=False)