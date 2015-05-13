__author__ = 'Ralph'


class Config(object):

    def __init__(self):
        self._config = dict()
        self._config_file_name = ''

    def load(self, file_name):
        f = open(file_name, 'r')
        for line in f.readlines():
            line = line.strip()
            if line.startswith('#') or line == '':
                continue
            parts = line.split('=')
            parts = [part.strip() for part in parts]
            self._config[parts[0]] = parts[1]
        f.close()
        self._config_file_name = file_name

    def get(self, key, default=None):
        try:
            value = self._config[key]
            if value == '':
                return None
            return value
        except KeyError:
            return default

    def get_bool(self, key, default=False):
        try:
            value = self._config[key].upper()
            if value == 'FALSE' or value == 'F':
                return False
            if value == 'TRUE' or value == 'T':
                return True
            raise ValueError('Illegal value: ' + value)
        except KeyError:
            return default

    def get_int(self, key, default=-1):
        try:
            return int(self._config[key])
        except KeyError:
            return default

    def get_float(self, key, default=0.0):
        try:
            return float(self._config[key])
        except KeyError:
            return default

    def get_list(self, key):
        try:
            value = self._config[key]
            parts = value.split(',')
            parts = [part.strip() for part in parts]
            try:
                # Try to convert to float. If this works, return
                # a list of floats. Otherwise, return list of strings
                float(parts[0])
                return [float(part) for part in parts]
            except ValueError:
                pass
            return parts
        except KeyError:
            return None

    def get_replace(self, key, identifiers):
        # If string identifier, search for {} and replace it. Otherwise,
        # it should be a list identifier and we search for numbered {?}
        # where ? ranges from 0 to some number.
        if type(identifiers) is str:
            return self.get(key).replace('{}', identifiers)
        elif type(identifiers) is list:
            value = self.get(key)
            for i in range(len(identifiers)):
                value = value.replace('{' + str(i) + '}', identifiers[i])
            return value
        # If neither a string nor list was provided raise exception
        raise TypeError('Parameter \'identifiers\' must be of string or list type')

    def set(self, key, value):
        if type(value) is bool:
            value = str(value).upper()
        elif type(value) is list:
            value = [str(v) for v in value]
            value = ','.join(value)
        else:
            value = str(value)
        self._config[key] = value

    def to_string(self):
        content = ''
        for key in sorted(self._config.keys()):
            content += key + ' = ' + self._config[key] + '\n'
        return content