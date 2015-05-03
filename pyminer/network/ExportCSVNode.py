__author__ = 'Ralph'

import os
import pandas as pd

from Node import Node
from InputPort import InputPort


class ExportCSVNode(Node):

    def __init__(self):
        """
        Constructor of this node
        :return:
        """
        super(ExportCSVNode, self).__init__('ExportCSV')

        self.add_input_port(
            InputPort(name='input', data_type=pd.DataFrame))
        self.set_required_config_items(['file_name'])

    def execute(self):
        """
        Executes this node
        :return:
        """
        self.check_config()

        file_name = self.get_config().get('file_name')
        data = self.get_input_port('input').get_data()
        if data is not None:
            data.to_csv(file_name, index=False)