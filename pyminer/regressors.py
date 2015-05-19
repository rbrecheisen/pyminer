__author__ = 'Ralph'

import pandas as pd

from base import Node
from base import InputPort
from base import OutputPort


class Regressor(Node):

    def __init__(self, name):

        super(Regressor, self).__init__(name)
        self.add_input_port(
            InputPort(name='input', data_type=pd.DataFrame))
        self.add_output_port(
            OutputPort(name='mode', data_type=str))
        self.add_output_port(
            OutputPort(name='performance', data_type=str))


class LinearRegression(Regressor):

    def __init__(self):

        super(LinearRegression, self).__init__('LinearRegression')

    def execute(self):
        pass


class SupportVectorRegression(Regressor):

    def __init__(self):

        super(SupportVectorRegression, self).__init__('SupportVectorRegression')

    def execute(self):
        pass


class GaussianProcesses(Regressor):

    def __init__(self):

        super(GaussianProcesses, self).__init__('GaussianProcesses')

    def execute(self):
        pass