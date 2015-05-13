__author__ = 'Ralph'

import pandas as pd

from base import Node
from base import InputPort


class ExportNode(Node):

    def __init__(self, name):
        super(ExportNode, self).__init__(name)


class ExportCSVNode(ExportNode):

    def __init__(self):

        super(ExportCSVNode, self).__init__('ExportCSV')
        self.add_input_port(InputPort(name='input', data_type=pd.DataFrame))
        self.set_required_config_items(['file_name'])

    def execute(self):

        self.check_config()
        file_name = self.get_config().get('file_name')
        data = self.get_input_port('input').get_data()
        if data is not None:
            data.to_csv(file_name, index=False)