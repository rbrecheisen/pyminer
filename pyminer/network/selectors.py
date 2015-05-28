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

        # Set configuration items for this node
        self.get_config().set('selector_type', None)
        self.get_config().set('selector_types', ['all', 'single', 'subset'])
        self.get_config().set('attributes', None)
        self.get_config().set('invert_selector', False)

    def execute(self):

        selector_types = self.get_config().get_list('selector_types')
        if selector_types is None:
            raise RuntimeError('Selector types not available')

        selector_type = self.get_config().get('selector_type')
        if selector_type is None:
            raise RuntimeError('Selector type not specified')
        if selector_type not in selector_types:
            raise RuntimeError('Unknown selector type ' + selector_type)

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
            attributes = self.get_config().get_list('attributes')
            if attributes is None:
                raise RuntimeError('Parameter \'attributes\' is missing')
            if len(attributes) == 0:
                raise RuntimeError('Attribute list is empty')
            if invert_selector:
                data_new = data[[attributes[0]]]
                self.get_output_port('output').set_data(data_new)
            else:
                data_new = data.drop(attributes[0], axis=1, inplace=False)
                self.get_output_port('output').set_data(data_new)

        elif selector_type == 'subset':
            attributes = self.get_config().get_list('attributes')
            if attributes is None:
                raise RuntimeError('Parameter \'attributes\' is missing')
            if len(attributes) == 0:
                raise RuntimeError('Attribute list is empty')
            if invert_selector:
                data_new = data[attributes]
                self.get_output_port('output').set_data(data_new)
            else:
                data_new = data.drop(attributes, axis=1, inplace=False)
                self.get_output_port('output').set_data(data_new)
        else:
            raise RuntimeError('ERROR: unknown selector type ' + selector_type)


class RemoveUselessAttributes(Selector):
    pass


class ReorderAttributes(Selector):
    pass


class RemoveCorrelatedAttributes(Selector):
    pass