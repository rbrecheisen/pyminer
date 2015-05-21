__author__ = 'Ralph'

import pandas as pd

from base import Node
from base import InputPort
from base import OutputPort


class Classifier(Node):

    def __init__(self, name):

        super(Classifier, self).__init__(name)
        self.add_input_port(
            InputPort(name='input', data_type=pd.DataFrame))
        self.add_output_port(
            OutputPort(name='model', data_type=str))
        self.add_output_port(
            OutputPort(name='performance', data_type=str))


class SupportVectorMachine(Classifier):

    def __init__(self):

        super(SupportVectorMachine, self).__init__('SupportVectorMachine')
        self.set_required_config_items(['kernel_type'])
        self._kernel_types = ['linear', 'rbf']

    def execute(self):

        self.check_config()
        kernel_type = self.get_config().get('kernel_type')
        if kernel_type not in self._kernel_types:
            raise RuntimeError('Kernel type ' + kernel_type + ' not supported')

        auto_detect = self.get_config().get_bool('auto_detect', True)

        if kernel_type == 'rbg':
            if not auto_detect:
                gamma = self.get_config().get_float('kernel_type.rbf.gamma')
                if gamma is None:
                    raise RuntimeError('Property \'gamma\' missing')


class GaussianProcesses(Classifier):

    def __init__(self):

        super(GaussianProcesses, self).__init__('GaussianProcesses')

    def execute(self):
        pass


class RandomForests(Classifier):

    def __init__(self):

        super(RandomForests, self).__init__('RandomForests')

    def execute(self):
        pass