__author__ = 'Ralph'

from base import Node


class Converter(Node):
    """
    Converts features values from one format to another.
    """
    pass


class NumericalToBinominal(Converter):
    pass


class NominalToBinominal(Converter):
    pass


class GuessTypes(Converter):
    pass


class NumericalToPolynominal(Converter):
    pass


class NominalToNumerical(Converter):
    pass


class TextToNominal(Converter):
    pass


class NumericalToReal(Converter):
    pass


class NumericalToDate(Converter):
    pass


class RealToInteger(Converter):
    pass


class NominalToText(Converter):
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