__author__ = 'Ralph'

import pandas as pd

from Node import Node
from InputPort import InputPort


class ExportCsvNode(Node):

    def __init__(self):
        """
        Constructor of this node.
        :return:
        """
        super(ExportCsvNode, self).__init__('ExportCSV')
        self.add_input_port(
            InputPort(name='input', data_type=pd.DataFrame))

    def execute(self):
        """
        Executes this node
        :return:
        """
        file_name = self.get_config().get('file_name')
        data = self.get_input_port('input').get_data()
        data.to_csv(file_name)