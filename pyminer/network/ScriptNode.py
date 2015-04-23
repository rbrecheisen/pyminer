__author__ = 'Ralph'

import sys
import StringIO

from Node import Node


class ScriptNode(Node):

    def __init__(self):
        """
        Constructor of this node.
        :return:
        """
        super(ScriptNode, self).__init__('Script')
        self.set_required_config_items(['text'])

    def execute(self):
        """
        Executes this node.
        :return:
        """
        self.check_config()

        exec self.get_config().get('text')