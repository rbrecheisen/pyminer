__author__ = 'Ralph'

import pandas as pd

from base import Node
from base import InputPort
from base import OutputPort


class FilterNode(Node):

    def __init__(self, name):
        super(FilterNode, self).__init__(name)
        self.add_input_port(
            InputPort(name='input', data_type=pd.DataFrame))
        self.add_output_port(
            OutputPort(name='output', data_type=pd.DataFrame))
        self.add_output_port(
            OutputPort(name='original', data_type=pd.DataFrame))
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
                pass
            else:
                pass
        elif filter_type == 'single':
            if invert_filter:
                pass
            else:
                pass
        elif filter_type == 'subset':
            if invert_filter:
                pass
            else:
                pass
        else:
            print('ERROR: unknown filter type ' + filter_type)


class FilterAttributesNode(FilterNode):

    def __init__(self):
        super(FilterAttributesNode, self).__init__('FilterAttributes')

    def execute(self):
        pass


class FilterExamplesNode(FilterNode):

    def __init__(self):
        super(FilterExamplesNode, self).__init__('FilterExamples')

    def execute(self):
        pass