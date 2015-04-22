__author__ = 'Ralph'

import pandas as pd

from Node import Node
from InputPort import InputPort
from OutputPort import OutputPort


class FilterExamplesNode(Node):

    def __init__(self):
        """
        Constructor of this node.
        :return:
        """
        super(FilterExamplesNode, self).__init__('FilterExamples')

        self.add_input_port(
            InputPort(name='input', data_type=pd.DataFrame))
        self.add_output_port(
            OutputPort(name='output', data_type=pd.DataFrame))

    def execute(self):
        """
        Executes this node.
        :return:
        """
        data = self.get_input_port('input').get_data()
        self.get_output_port('output').set_data(data)