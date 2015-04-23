__author__ = 'Ralph'

import pandas as pd

from Node import Node
from InputPort import InputPort
from OutputPort import OutputPort


class FilterAttributesNode(Node):

    def __init__(self):
        """
        Constructor of this node.
        :return:
        """
        super(FilterAttributesNode, self).__init__('FilterAttributes')

        self.add_input_port(
            InputPort(name='input', data_type=pd.DataFrame))
        self.add_output_port(
            OutputPort(name='output', data_type=pd.DataFrame))
        self.add_output_port(
            OutputPort(name='original', data_type=pd.DataFrame))

        self.set_required_config_items(['filter_type'])
        self._filter_types = [
            'all', 'single', 'subset', 'regexp', 'value_type', 'no_missing_values']

    def execute(self):
        """
        Executes this node
        :return:
        """
        self.check_config()

        # Check if filter type supported
        filter_type = self.get_config().get('filter_type')
        if filter_type not in self._filter_types:
            raise RuntimeError('Unknown filter type \'' + filter_type + '\'')

        # Get invert filter configuration. If item not set, defaults to False
        invert_filter = self.get_config().get_bool('invert_filter')

        # Get input data frame
        data = self.get_input_port('input').get_data()

        # Process data depending on selected filter type
        if filter_type == 'all':
            if invert_filter:
                # Pass data unchanged to output port
                self.get_output_port('output').set_data(data)
            else:
                # Filter everything, that is, don't let anything through
                self.get_output_port('output').set_data(None)

        elif filter_type == 'single':
            attribute = self.get_config().get('filter_type.single')
            if attribute is None:
                raise RuntimeError('Required filter option \'filter_type.single\' missing')
            if invert_filter:
                # Select attribute column
                data_new = data[[attribute]]
            else:
                # Get indexes of all attribute columns except selected one
                indexes = data.columns[data.columns != attribute]
                data_new = data[indexes]
            # Pass new data frame to output port
            self.get_output_port('output').set_data(data_new)

        elif filter_type == 'subset':
            attributes = self.get_config().get_list('filter_type.subset')
            if len(attributes) == 0:
                raise RuntimeError('Required filter option \'filter_type.subset\' empty')
            if invert_filter:
                # Select attribute columns
                data_new = data[attributes]
            else:
                # Select all attribute columns except selected ones
                data_new = data.drop(attributes, axis=1, inplace=False)
            self.get_output_port('output').set_data(data_new)

        elif filter_type == 'regexp':
            raise RuntimeError('Filter type \'regexp\' not implemented yet')

        elif filter_type == 'value_type':
            raise RuntimeError('Filter type \'value_type\' not implemented yet')

        elif filter_type == 'no_missing_values':
            raise RuntimeError('Filter type \'no_missing_value\' not implemented yet')

        # Pass data unchanged to 'original' port
        self.get_output_port('original').set_data(data)