__author__ = 'Ralph'

from Port import Port


class InputPort(Port):

    def __init__(self, name, data_type):
        """
        Constructor of this input port
        :param name: Port name
        :param data_type: Data type
        :return:
        """
        super(InputPort, self).__init__(name, data_type)

    def get_data(self):
        """
        Returns data associated with its connection. Currently
        we directly get the data from the connection's source
        which is the output port of the connected node.
        :return: Input data
        """
        connection = self.get_connection()
        if not connection is None:
            return self.get_connection().get_source().get_data()
        return None