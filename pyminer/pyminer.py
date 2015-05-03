__author__ = 'Ralph'

from network.ImportCSVNode import ImportCSVNode
from network.FilterAttributesNode import FilterAttributesNode
from network.ExportCSVNode import ExportCSVNode
from network.Connection import Connection

# from ui.Application import Application


def get_data_root():
    return '../tests/data/'


if __name__ == '__main__':

    # Create nodes

    node1 = ImportCSVNode()
    node2 = FilterAttributesNode()
    node3 = ExportCSVNode()

    # Configure nodes

    node1.get_config().add('file_name', get_data_root() + 'file.csv')

    node2.get_config().add('filter_type', 'subset')
    node2.get_config().add('filter_type.subset', 'id,name')
    node2.get_config().add('invert_filter', False)

    node3.get_config().add('file_name', get_data_root() + 'file_new.csv')

    # Setup connections

    connection1 = Connection(
        node1.get_output_port('output'), node2.get_input_port('input'))
    connection2 = Connection(
        node2.get_output_port('output'), node3.get_input_port('input'))

    # Execute network

    node1.execute()

    # Run application

    # application = Application()
    # application.run()