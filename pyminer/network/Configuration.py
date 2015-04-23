__author__ = 'Ralph'


class Configuration(object):

    def __init__(self):
        """
        Constructor of this configuration.
        :return:
        """
        self._items = dict()

    def add(self, key, value):
        """
        Add a configuration item with given value.
        :param key: Configuration item
        :param value: Value
        :return:
        """
        self._items[key] = value

    def remove(self, key):
        """
        Remove given configuration item from configuration
        :param key: Configuration item
        :return:
        """
        try:
            del self._items[key]
        except KeyError:
            pass

    def get(self, key):
        """
        Returns configuration item of given name or None if
        it does not exist.
        :param key: Configuration item
        :return: Configuration value
        """
        try:
            return self._items[key]
        except KeyError:
            return None

    def get_int(self, key, default=-1):
        """
        Returns configuration item as integer or default
        value if any error occurs.
        :param key: Configuration item
        :param default: Default value
        :return: Item
        """
        value = self.get(key)
        try:
            return int(value)
        except (TypeError, ValueError):
            return default

    def get_float(self, key, default=0.0):
        """
        Returns configuration item as float or default
        value if any error occurs.
        :param key: Configuration item
        :param default: Default value
        :return: Item
        """
        value = self.get(key)
        try:
            return float(value)
        except (TypeError, ValueError):
            return default

    def get_bool(self, key, default=False):
        """
        Returns configuration item as bool or default
        value if any error occurs.
        :param key: Configuration item
        :param default: Default value
        :return: Item
        """
        value = self.get(key)
        try:
            return bool(value)
        except (TypeError, ValueError):
            return default

    def get_list(self, key):
        """
        Returns configuration item as list or default
        value if any error occurs.
        :param key: Configuration item
        :param default: Default value
        :return: Item
        """
        value = self.get(key)
        try:
            parts = value.split(',')
            return parts
        except (TypeError, ValueError):
            return []