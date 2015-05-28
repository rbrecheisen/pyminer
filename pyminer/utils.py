__author__ = 'Ralph'

import time
import datetime


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

    def get_number_of_items(self):
        return len(self._config.keys())

    def get_keys(self):
        return self._config.keys()

    def to_string(self):
        content = ''
        for key in sorted(self._config.keys()):
            content += key + ' = ' + self._config[key] + '\n'
        return content


class Log(object):

    log_file = None
    log_to_std_out = True

    @staticmethod
    def set_log_file(file_name):
        Log.log_file = open(file_name, 'w')

    @staticmethod
    def set_log_to_std_out(log_to_std_out):
        Log.log_to_std_out = log_to_std_out

    @staticmethod
    def info(message):
        now = Timing.get_now_as_string()
        if Log.log_to_std_out:
            print(now + ' INFO: ' + message)
        Log.log_file.write(now + ' INFO: ' + message + '\n')

    @staticmethod
    def warning(message):
        now = Timing.get_now_as_string()
        if Log.log_to_std_out:
            print(now + ' WARNING: ' + message)
        Log.log_file.write(now + ' WARNING: ' + message + '\n')

    @staticmethod
    def error(message):
        now = Timing.get_now_as_string()
        if Log.log_to_std_out:
            print(now + ' ERROR: ' + message)
        Log.log_file.write(now + ' ERROR: ' + message + '\n')


class Timing(object):

    @staticmethod
    def get_now():
        """
        Returns current time
        :return: Time
        """
        return time.time()

    @staticmethod
    def get_now_as_string():
        """
        Returns current time in string format.
        :return: Time as string
        """
        t = time.time()
        return datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def get_elapsed(start_time):
        """
        Calculates hours, minutes and seconds elapsed between
        start time and now.
        :param start_time: Start time
        :return: Elapsed time
        """
        elapsed = Timing.get_now() - start_time
        nr_hours = int(elapsed / 3600)
        nr_minutes = int((elapsed - nr_hours * 3600) / 60)
        nr_seconds = int((elapsed - nr_hours * 3600 - nr_minutes * 60))
        nr_hours = '0' + str(nr_hours) if nr_hours < 10 else str(nr_hours)
        nr_minutes = '0' + str(nr_minutes) if nr_minutes < 10 else str(nr_minutes)
        nr_seconds = '0' + str(nr_seconds) if nr_seconds < 10 else str(nr_seconds)

        return nr_hours, nr_minutes, nr_seconds
