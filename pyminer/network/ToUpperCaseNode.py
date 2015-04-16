__author__ = 'Ralph'

from Node import Node
from InputPort import InputPort
from OutputPort import OutputPort


class ToUpperCaseNode(Node):

    def __init__(self):
        """
        Constuctor of this node.
        :return:
        """
        super(ToUpperCaseNode, self).__init__()

        self.add_input_port(
            InputPort(name='input', data_type=str))
        self.add_output_port(
            OutputPort(name='output', data_type=str))

    def execute(self):
        """
        Executes this node by reading the string data from
        its input port, converting it to upper case and passing
        it to the output port.
        :return:
        """
        data = self.get_input_port('input').get_data()
        data_new = data.upper()
        self.get_output_port('output').set_data(data_new)