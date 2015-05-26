__author__ = 'Ralph'

from pyminer.network.base import Node


class Cleaner(Node):
    pass


class ReplaceMissingValues(Cleaner):
    pass


class InputMissingValues(Cleaner):
    pass


class ReplaceInfiniteValues(Cleaner):
    pass


class FillGaps(Cleaner):
    pass


class RemoveUnusedValues(Cleaner):
    pass