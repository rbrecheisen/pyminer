__author__ = 'Ralph'

import pandas as pd

from base import Node
from base import InputPort
from base import OutputPort


class Selector(Node):

    def __init__(self, name):

        super(Selector, self).__init__(name)
        self.add_input_port(
            InputPort(name='input', data_type=pd.DataFrame))
        self.add_output_port(
            OutputPort(name='output', data_type=pd.DataFrame))


class SelectAttributes(Selector):

    def __init__(self):

        super(SelectAttributes, self).__init__('SelectAttributes')
        self.set_required_config_items(['filter_type'])
        self._filter_types = [
            'all', 'single', 'subset']

    def execute(self):

        self.check_config()

        filter_type = self.get_config().get('filter_type')
        if filter_type not in self._filter_types:
            raise RuntimeError('Unknown filter type ' + filter_type)

        invert_filter = self.get_config().get_bool('invert_filter', False)

        data = self.get_input_port('input').get_data()
        if data is None:
            return

        if filter_type == 'all':
            if invert_filter:
                self.get_output_port('output').set_data(data)
            else:
                self.get_output_port('output').set_data(None)

        elif filter_type == 'single':
            attribute = self.get_config().get('filter_type.single')
            if attribute is None:
                raise RuntimeError('Parameter \'filter_type.single\' is missing')
            if invert_filter:
                data_new = data[[attribute]]
                self.get_output_port('output').set_data(data_new)
            else:
                data_new = data.drop(attribute, axis=1, inplace=False)
                self.get_output_port('output').set_data(data_new)

        elif filter_type == 'subset':
            attributes = self.get_config().get_list('filter_type.subset')
            if attributes is None:
                raise RuntimeError('Parameter \'filter_type.subset\' is missing')
            if invert_filter:
                data_new = data[attributes]
                self.get_output_port('output').set_data(data_new)
            else:
                data_new = data.drop(attributes, axis=1, inplace=False)
                self.get_output_port('output').set_data(data_new)
        else:
            print('ERROR: unknown filter type ' + filter_type)


class RemoveUselessAttributes(Selector):
    pass


class ReorderAttributes(Selector):
    pass


class RemoveCorrelatedAttributes(Selector):
    pass