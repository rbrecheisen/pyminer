__author__ = 'Ralph'

from base import Node


class Selector(Node):
    """
    Select or remove attributes based on various criteria.
    """
    pass


class SelectAttributes(Selector):
    pass


class RemoveUselessAttributes(Selector):
    pass


class ReorderAttributes(Selector):
    pass


class RemoveCorrelatedAttributes(Selector):
    pass