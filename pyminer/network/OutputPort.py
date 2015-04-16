__author__ = 'Ralph'

from Port import Port


class OutputPort(Port):

    def __init__(self, name, data_type):
        """
        Constructor of this output port.
        :param name: Port name
        :param data_type: Data type
        :return:
        """
        super(OutputPort, self).__init__(name, data_type)
        self._data = None

    def get_data(self):
        """
        Returns data associated with this output port
        :return: Output data
        """
        return self._data

    def set_data(self, data):
        """
        Sets data of this output port. The current implementation
        directly calls the next node's execute() function through
        the shared connection object. The data type is also stored
        :param data: Output data
        :return:
        """
        self._data = data
        connection = self.get_connection()
        if not connection is None:
            connection.get_target().get_node().execute()