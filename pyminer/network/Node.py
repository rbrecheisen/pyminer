__author__ = 'Ralph'

from InputPort import InputPort
from OutputPort import OutputPort
from Configuration import Configuration


class Node(object):

    def __init__(self, name):
        """
        Constructor of this node.
        :param name: Name of this node
        :return:
        """
        self._name = name
        self._input_ports = dict()
        self._output_ports = dict()
        self._configuration = Configuration()
        self._required_config_items = list()

    def get_name(self):
        """
        Returns name of this node
        :return: Name
        """
        return self._name

    def set_name(self, name):
        """
        Sets name of this node
        :param name: Name
        :return:
        """
        self._name = name

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

    def get_config(self):
        """
        Returns configuration of this node.
        :return: Configuration
        """
        return self._configuration

    def get_required_config_items(self):
        """
        Returns required configuration items.
        :return: Configuration items
        """
        return self._required_config_items

    def set_required_config_items(self, items):
        """
        Adds list required configuration items which the node needs
        to execute. The node will check for these items before
        running execute.
        :param keys: List of mandatory configuration items
        :return:
        """
        self._required_config_items = items

    def check_config(self):
        """
        Checks whether configuration contains all the required
        items. Any other items are optional.
        :return:
        """
        for item in self.get_required_config_items():
            value = self.get_config().get(item)
            if value is None:
                raise RuntimeError('Missing required configuration item \'' + item + '\'')

    def execute(self):
        """
        Executes this node. Must be implemented by child classes
        :return:
        """
        raise RuntimeError('Not implemented')