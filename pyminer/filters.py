__author__ = 'Ralph'

import pandas as pd

from base import Node
from base import InputPort
from base import OutputPort


class Filter(Node):

    def __init__(self, name):

        super(Filter, self).__init__(name)
        self.add_input_port(
            InputPort(name='input', data_type=pd.DataFrame))
        self.add_output_port(
            OutputPort(name='output', data_type=pd.DataFrame))


class FilterExamples(Filter):

    def __init__(self):

        super(FilterExamples, self).__init__('FilterExamples')
        self.set_required_config_items(['filter_type'])
        self._filter_types = ['all']

    def execute(self):

        self.check_config()

        data = self.get_input_port('input').get_data()
        if data is None:
            return

        self.get_output_port('output').set_data(data)


class FilterExampleRange(Filter):
    pass


class RemoveDuplicates(Filter):
    pass