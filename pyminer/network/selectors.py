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
        self.set_required_config_items(['selector_type'])
        self._selector_types = ['all', 'single', 'subset']

    def execute(self):

        self.check_config()

        selector_type = self.get_config().get('selector_type')
        if selector_type not in self._selector_types:
            raise RuntimeError('Unknown filter type ' + selector_type)

        invert_selector = self.get_config().get_bool('invert_selector', False)

        data = self.get_input_port('input').get_data()
        if data is None:
            return

        if selector_type == 'all':
            if invert_selector:
                self.get_output_port('output').set_data(data)
            else:
                self.get_output_port('output').set_data(None)

        elif selector_type == 'single':
            attribute = self.get_config().get_list('attributes')[0]
            if attribute is None:
                raise RuntimeError('Parameter \'attributes\' is missing')
            if invert_selector:
                data_new = data[[attribute]]
                self.get_output_port('output').set_data(data_new)
            else:
                data_new = data.drop(attribute, axis=1, inplace=False)
                self.get_output_port('output').set_data(data_new)

        elif selector_type == 'subset':
            attributes = self.get_config().get_list('attributes')
            if attributes is None:
                raise RuntimeError('Parameter \'attributes\' is missing')
            if invert_selector:
                data_new = data[attributes]
                self.get_output_port('output').set_data(data_new)
            else:
                data_new = data.drop(attributes, axis=1, inplace=False)
                self.get_output_port('output').set_data(data_new)
        else:
            print('ERROR: unknown selector type ' + selector_type)


class RemoveUselessAttributes(Selector):
    pass


class ReorderAttributes(Selector):
    pass


class RemoveCorrelatedAttributes(Selector):
    pass