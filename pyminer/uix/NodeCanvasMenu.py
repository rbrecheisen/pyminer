__author__ = 'Ralph'

import wx


class NodeCanvasMenu(wx.Menu):

    def __init__(self, parent):
        """
        Constructor for this menu.
        :param parent: Parent widget of this menu
        :return:
        """
        super(NodeCanvasMenu, self).__init__()

        self._parent = parent
        item = wx.MenuItem(self, wx.NewId(), 'Create Node')

        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self._on_create_node, item)

    def _on_create_node(self, e):
        """
        Called when user has selected 'Create Node' item
        :param e: Event object
        :return:
        """
        self._parent.create_node()