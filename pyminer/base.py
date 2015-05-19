__author__ = 'Ralph'

from utils import Config


class Node(object):

    def __init__(self, name):

        self._name = name
        self._config = Config()
        self._required_config_items = list()
        self._input_ports = dict()
        self._output_ports = dict()

    def get_name(self):

        return self._name

    def set_name(self, name):

        self._name = name

    def add_input_port(self, port):

        if not isinstance(port, InputPort):
            raise RuntimeError('Port must be of type InputPort')
        self._input_ports[port.get_name()] = port
        self._input_ports[port.get_name()].set_node(self)

    def get_input_port(self, name):

        return self._input_ports[name]

    def add_output_port(self, port):

        if not isinstance(port, OutputPort):
            raise RuntimeError('Port must be of type OutputPort')
        self._output_ports[port.get_name()] = port
        self._output_ports[port.get_name()].set_node(self)

    def get_output_port(self, name):

        return self._output_ports[name]

    def get_config(self):

        return self._config

    def get_required_config_items(self):

        return self._required_config_items

    def set_required_config_items(self, required_config_items):

        self._required_config_items = required_config_items

    def check_config(self):

        for item in self.get_required_config_items():
            value = self.get_config().get(item)
            if value is None:
                raise RuntimeError('Missing required config item \'' + item + '\'')

    def execute(self):

        raise RuntimeError('Not implemented')

    @staticmethod
    def print_help():

        raise RuntimeError('Not implemented')


class Port(object):

    def __init__(self, name, data_type):

        self._name = name
        self._data_type = data_type
        self._node = None
        self._connection = None
        self._description = ''

    def get_name(self):

        return self._name

    def set_name(self, name):

        self._name = name

    def get_node(self):

        return self._node

    def set_node(self, node):

        self._node = node

    def get_connection(self):

        return self._connection

    def set_connection(self, connection):

        self._connection = connection

    def get_data_type(self):

        return self._data_type

    def get_data(self):

        raise RuntimeError('Not implemented')

    def get_description(self):

        return self._description

    def set_description(self, description):

        self._description = description


class InputPort(Port):

    def __init__(self, name, data_type):

        super(InputPort, self).__init__(name, data_type)

    def get_data(self):

        connection = self.get_connection()
        if connection is not None:
            return self.get_connection().get_source().get_data()
        return None


class OutputPort(Port):

    def __init__(self, name, data_type):

        super(OutputPort, self).__init__(name, data_type)
        self._data = None

    def get_data(self):

        return self._data

    def set_data(self, data):

        self._data = data
        connection = self.get_connection()
        if connection is not None:
            connection.get_target().get_node().execute()


class Connection(object):

    def __init__(self, source, target):

        if not isinstance(source, OutputPort):
            raise RuntimeError('Source must be of type OutputPort')
        if not isinstance(target, InputPort):
            raise RuntimeError('Target must be of type InputPort')
        if not source.get_data_type() is target.get_data_type():
            raise RuntimeError('Source and target data types must be the same')
        self._source = source
        self._source.set_connection(self)
        self._target = target
        self._target.set_connection(self)

    def get_source(self):

        return self._source

    def get_target(self):

        return self._target