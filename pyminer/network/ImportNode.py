__author__ = 'Ralph'

from Node import Node
from OutputPort import OutputPort


class ImportNode(Node):

    def __init__(self):
        """
        Constructor of this import node.
        :return:
        """
        super(ImportNode, self).__init__()
        self.add_output_port(OutputPort(name='output', data_type=str))

    def execute(self):
        """
        Executes import node by creating a string and sending
        it to its output port.
        :return:
        """
        data = 'This is some data string'
        port = self.get_output_port('output')
        port.set_data(data)