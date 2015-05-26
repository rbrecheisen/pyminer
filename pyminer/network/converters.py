__author__ = 'Ralph'

import pandas as pd

from pyminer.network.base import Node
from pyminer.network.base import InputPort
from pyminer.network.base import OutputPort


class Converter(Node):

    def __init__(self, name):

        super(Converter, self).__init__(name)
        self.add_input_port(
            InputPort(name='input', data_type=pd.DataFrame))
        self.add_output_port(
            OutputPort(name='output', data_type=pd.DataFrame))
        self.set_required_config_items(['attributes'])


class NumericalToBinominal(Converter):

    def __init__(self):

        super(NumericalToBinominal, self).__init__('NumericalToBinominal')

    def execute(self):

        self.check_config()
        data = self.get_input_port('input').get_data()
        if data is None:
            return

        attributes = self.get_config().get_list('attributes')
        for attribute in attributes:
            column = data[attribute]
            if column.nunique() != 2:
                print('WARNING: attribute ' + attribute + ' has more than 2 values')
                continue

            # todo: continue here


class BinominalToNumerical(Converter):

    def __init__(self):

        super(BinominalToNumerical, self).__init__('BinominalToNumerical')

    def execute(self):

        self.check_config()
        data = self.get_input_port('input').get_data()
        if data is None:
            return

        attributes = self.get_config().get_list('attributes')
        for attribute in attributes:
            if data[attribute].nunique() != 2:
                raise RuntimeError('Attribute is not binominal')
            data[attribute] = pd.Categorical(data[attribute]).codes

        self.get_output_port('output').set_data(data)


class NumericalToNominal(Converter):

    def __init__(self):

        super(NumericalToNominal, self).__init__('NumericalToNominal')

    def execute(self):

        self.check_config()
        data = self.get_input_port('input').get_data()
        if data is None:
            return

        attributes = self.get_config().get_list('attributes')


class NominalToNumerical(Converter):

    def __init__(self):

        super(NominalToNumerical, self).__init__('NominalToNumerical')

    def execute(self):

        self.check_config()
        data = self.get_input_port('input').get_data()
        if data is None:
            return

        attributes = self.get_config().get_list('attributes')


class TextToNominal(Converter):
    pass


class NominalToText(Converter):
    pass


class NumericalToDate(Converter):
    pass


class RealToInteger(Converter):
    pass


class IntegerToReal(Converter):
    pass


class FormatNumbers(Converter):
    pass


class DiscretizeByBinning(Converter):
    pass


class DiscretizeByFrequency(Converter):
    pass


class DiscretizeBySize(Converter):
    pass


class DiscretizeByEntropy(Converter):
    pass


class DiscretizeByUserSpecification(Converter):
    pass


class GuessTypes(Converter):
    pass