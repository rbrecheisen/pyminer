__author__ = 'Ralph'

from InputPort import InputPort
from OutputPort import OutputPort


class Connection(object):

    def __init__(self, source, target):
        """
        Constructor of this connection.
        :param source: Output port of a node
        :param target: Input port of a node
        :return:
        """
        if not type(source) is OutputPort:
            raise RuntimeError('Source must be of type OutputPort')
        if not type(target) is InputPort:
            raise RuntimeError('Target must be of type InputPort')
        if not source.get_data_type() is target.get_data_type():
            raise RuntimeError('Source and target data types must be the same')

        self._source = source
        self._source.set_connection(self)
        self._target = target
        self._target.set_connection(self)

    def get_source(self):
        """
        Returns output port of connected node
        :return: Output port
        """
        return self._source

    def get_target(self):
        """
        Returns input port of connected node
        :return: Input port
        """
        return self._target