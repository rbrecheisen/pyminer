__author__ = 'Ralph'

import wx


class NodeMenu(wx.Menu):

    def __init__(self, parent, node):
        """
        Constructor for this menu.
        :param parent: Parent widget of this menu
        :param node: Node this menu belongs to
        :return:
        """
        super(NodeMenu, self).__init__()

        self._parent = parent
        self._node = node

        item = wx.MenuItem(self, wx.NewId(), 'Delete Node')
        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self._on_delete_node, item)

    def _on_delete_node(self, e):
        """
        Called when user has selected 'Create Node' item
        :param e: Event object
        :return:
        """
        self._parent.delete_node(self._node)