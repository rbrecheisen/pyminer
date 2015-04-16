__author__ = 'Ralph'

from network.ImportNode import ImportNode
from network.ExportNode import ExportNode
from network.ToUpperCaseNode import ToUpperCaseNode
from network.Connection import Connection

from ui.ApplicationWindow import ApplicationWindow


if __name__ == '__main__':

    # Setup nodes

    node1 = ImportNode()
    node2 = ToUpperCaseNode()
    node3 = ExportNode()

    # Setup connections

    connection1 = Connection(
        node1.get_output_port('output'), node2.get_input_port('input'))
    connection2 = Connection(
        node2.get_output_port('output'), node3.get_input_port('input'))

    # Execute network

    node1.execute()