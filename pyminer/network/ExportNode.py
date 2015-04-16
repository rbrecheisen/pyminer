__author__ = 'Ralph'

from Node import Node
from InputPort import InputPort


class ExportNode(Node):

    def __init__(self):
        """
        Constructor of this export node
        :return:
        """
        super(ExportNode, self).__init__()
        self.add_input_port(InputPort(name='input', data_type=str))

    def execute(self):
        """
        Executes this node by retrieving data from its input
        port and printing it to the console.
        :return:
        """
        data = self.get_input_port('input').get_data()
        print(data)