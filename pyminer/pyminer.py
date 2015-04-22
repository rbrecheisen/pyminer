__author__ = 'Ralph'

from network.ImportCsvNode import ImportCsvNode
from network.FilterExamplesNode import FilterExamplesNode
from network.ExportCsvNode import ExportCsvNode
from network.Connection import Connection

from ui.Application import Application


if __name__ == '__main__':

    # Create nodes

    node1 = ImportCsvNode()
    node2 = FilterExamplesNode()
    node3 = ExportCsvNode()

    # Configure nodes

    node1.get_config().add('file_name', 'file.csv')
    node3.get_config().add('file_name', 'file_new.csv')

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