__author__ = 'Ralph'

from InputPort import InputPort
from OutputPort import OutputPort


class Node(object):

    def __init__(self):
        """
        Constructor of this node.
        :return:
        """
        self._input_ports = dict()
        self._output_ports = dict()

    def add_input_port(self, port):
        """
        Adds new input port to this node
        :param port: Input port
        :return:
        """
        if not type(port) is InputPort:
            raise RuntimeError('Port must be of type InputPort')

        self._input_ports[port.get_name()] = port
        self._input_ports[port.get_name()].set_node(self)

    def get_input_port(self, name):
        """
        Returns input port of given name.
        :param name: Port name
        :return: Input port
        """
        return self._input_ports[name]

    def add_output_port(self, port):
        """
        Adds new output port to this node.
        :param port: Output port
        :return:
        """
        if not type(port) is OutputPort:
            raise RuntimeError('Port must be of type OutputPort')

        self._output_ports[port.get_name()] = port
        self._output_ports[port.get_name()].set_node(self)

    def get_output_port(self, name):
        """
        Returns output port of given name.
        :param name: Port name
        :return: Output port
        """
        return self._output_ports[name]

    def execute(self):
        """
        Executes this node. Must be implemented by child classes
        :return:
        """
        raise RuntimeError('Not implemented')