__author__ = 'Ralph'


class Configuration(object):

    def __init__(self):
        """
        Constructor of this configuration.
        :return:
        """
        self._items = dict()

    def add(self, key, value):
        self._items[key] = value

    def remove(self, key):
        del self._items[key]

    def get(self, key):
        return self._items[key]

    def get_int(self, key, default=-1):
        try:
            value = self.get[key]
            return int(value)
        except KeyError:
            return default

    def get_float(self, key, default=0.0):
        try:
            value = self.get[key]
            return float(value)
        except KeyError:
            return default

    def get_bool(self, key, default=False):
        try:
            value = self.get[key]
            return bool(value)
        except KeyError:
            return default

    def get_list(self, key):
        try:
            value = self.get[key]
            parts = value.split(',')
            return parts
        except KeyError:
            return []