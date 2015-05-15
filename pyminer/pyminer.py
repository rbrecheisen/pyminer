__author__ = 'Ralph'

# from ui.Application import Application

from base import Connection
from importers import ImportCSV
from exporters import ExportCSVNode
from filters import FilterAttributesNode


def get_data_root():
    return '../tests/data/'


if __name__ == '__main__':

    node1 = ImportCSV()
    node2 = FilterAttributesNode()
    node3 = ExportCSVNode()

    node1.get_config().set('file_name', get_data_root() + 'file.csv')
    node2.get_config().set('filter_type', 'subset')
    node2.get_config().set('filter_type.subset', ['id', 'name'])
    node2.get_config().set('invert_filter', True)
    node3.get_config().set('file_name', get_data_root() + 'file_new.csv')

    connection1 = Connection(
        node1.get_output_port('output'), node2.get_input_port('input'))
    connection2 = Connection(
        node2.get_output_port('output'), node3.get_input_port('input'))

    node1.execute()