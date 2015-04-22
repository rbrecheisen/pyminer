__author__ = 'Ralph'

import pandas as pd

from Node import Node
from OutputPort import OutputPort


class ImportCsvNode(Node):

    def __init__(self):
        """
        Constructor of this node.
        :return:
        """
        super(ImportCsvNode, self).__init__('ImportCSV')
        self.add_output_port(OutputPort(name='output', data_type=pd.DataFrame))

    def execute(self):
        """
        Executes this node by importing the CSV file
        in its parameter settings
        :return:
        """
        file_name = self.get_config().get('file_name')
        data_frame = pd.read_csv(file_name)
        port = self.get_output_port('output')
        port.set_data(data_frame)