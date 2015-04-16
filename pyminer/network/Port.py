__author__ = 'Ralph'


class Port(object):

    def __init__(self, name, data_type):
        """
        Constructor of this port.
        :param name: Port name
        :param data_type: Data type
        :return:
        """
        self._name = name
        self._data_type = data_type
        self._node = None
        self._connection = None

    def get_name(self):
        """
        Returns port name
        :return:
        """
        return self._name

    def get_node(self):
        """
        Returns node associated with this port.
        :return: Port node
        """
        return self._node

    def set_node(self, node):
        """
        Sets the node associated with this port.
        :param node: Port node
        :return:
        """
        self._node = node

    def get_connection(self):
        """
        Returns the connection associated with this
        port, or None
        :return: Port connection
        """
        return self._connection

    def set_connection(self, connection):
        """
        Sets connection associated with this port.
        :param connection: Port connection
        :return:
        """
        self._connection = connection

    def get_data(self):
        """
        Returns data associated with this port. Must be
        implemented in child classes.
        :return: Port data
        """
        raise RuntimeError('Not implemented')

    def get_data_type(self):
        """
        Returns data type associated with this port.
        :return: Data type
        """
        return self._data_type
