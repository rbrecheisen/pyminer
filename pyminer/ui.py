__author__ = 'Ralph'

import wx

from widgets import ImportCSVWidget

# todo: move widget list to main script?


class Application(wx.App):

    def __init__(self):

        super(Application, self).__init__()

        self._widgets = []
        self._widgets.append(ImportCSVWidget())
        self._window = ApplicationWindow('PyMiner v1.0', self._widgets)

    def run(self):

        self._window.Show()
        self._window.SetSize((800, 500))
        self.MainLoop()


class ApplicationWindow(wx.Frame):

    def __init__(self, title, widgets):

        super(ApplicationWindow, self).__init__(None, -1, title)

        self._widgets = widgets
        self._canvas = NodeViewCanvas(self, self._widgets)
        self.Bind(wx.EVT_CLOSE, self._close)

    def _close(self, event):

        for widget in self._widgets:
            widget.Destroy()
        self.Destroy()


class NodeView(object):

    def __init__(self, widget, position):

        super(NodeView, self).__init__()
        self._widget = widget
        self._dragging = False
        self._width = 50
        self._height = 50
        self._position = (0, 0)
        self.set_position(position)

    def get_node(self):

        return self.get_widget().get_node()

    def get_widget(self):

        return self._widget

    def is_dragging(self):

        return self._dragging

    def set_dragging(self, dragging):

        self._dragging = dragging

    def x(self):

        return self._position[0]

    def set_x(self, x):

        self._position = (x, self._position[1])
        return self._position

    def y(self):

        return self._position[1]

    def set_y(self, y):

        self._position = (self._position[0], y)

    def get_position(self):

        return self._position

    def set_position(self, position):

        self._position = (position[0] - self._width / 2, position[1] - self._height / 2)

    def width(self):

        return self._width

    def height(self):

        return self._height

    def contains(self, position):

        x = position[0]
        y = position[1]
        if self.x() < x < self.x() + self.width() and self.y() < y < self.y() + self.height():
            return True
        return False

    def render(self, device):

        device.SetPen(wx.Pen(wx.BLACK))
        device.SetBrush(wx.Brush(wx.RED))
        device.DrawEllipse(self.x(), self.y(), self.width(), self.height())


class NodeViewCanvas(wx.Panel):

    def __init__(self, parent, widgets):

        super(NodeViewCanvas, self).__init__(parent)

        self._widgets = widgets

        self.Bind(wx.EVT_PAINT, self._on_paint)
        self.Bind(wx.EVT_RIGHT_UP, self._show_menu)
        self.Bind(wx.EVT_LEFT_DOWN, self._start_drag)
        self.Bind(wx.EVT_LEFT_UP, self._stop_drag)
        self.Bind(wx.EVT_MOTION, self._move_node)
        self.Bind(wx.EVT_LEFT_DCLICK, self._show_dialog)

        self._node_views = []

    def create_node_view(self, widget):

        (x, y, width, height) = self.GetClientRect().Get()
        position = (x + width / 2, y + height / 2)
        self._node_views.append(NodeView(widget, position))
        self.Refresh()

    def delete_node_view(self, node):

        self._node_views.remove(node)
        self.Refresh()

    # EVENT HANDLERS

    def _on_paint(self, event):

        device = wx.PaintDC(self)
        for node_view in self._node_views:
            node_view.render(device)

    def _show_menu(self, event):

        position = event.GetPosition()
        menu = NodeViewCanvasMenu(self, self._widgets)
        for node_view in self._node_views:
            if node_view.contains(position):
                menu = NodeViewMenu(self, node_view)
                break
        self.PopupMenu(menu, event.GetPosition())

    def _start_drag(self, event):

        position = event.GetPosition()
        for node_view in self._node_views:
            node_view.set_dragging(False)
            if node_view.contains(position):
                node_view.set_dragging(True)
                break

    def _stop_drag(self, event):

        for node_view in self._node_views:
            node_view.set_dragging(False)

    def _move_node(self, event):

        for node_view in self._node_views:
            if node_view.is_dragging():
                node_view.set_position(event.GetPosition())
        self.Refresh()

    def _show_dialog(self, event):

        position = event.GetPosition()
        for node_view in self._node_views:
            if node_view.contains(position):
                node_view.get_widget().show()
                break


class NodeViewMenu(wx.Menu):

    def __init__(self, parent, node_view):

        super(NodeViewMenu, self).__init__()
        self._parent = parent
        self._node_view = node_view
        item = wx.MenuItem(self, wx.NewId(), 'Delete Node')
        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self._delete_node_view, item)

    # EVENT HANDLERS

    def _delete_node_view(self, event):

        self._parent.delete_node_view(self._node_view)


class NodeViewCanvasMenu(wx.Menu):

    def __init__(self, canvas, widgets):

        super(NodeViewCanvasMenu, self).__init__()

        self._canvas = canvas
        self._widget_ids = {}
        menu = wx.Menu()

        for widget in widgets:
            item = wx.MenuItem(self, wx.NewId(), widget.get_name())
            menu.AppendItem(item)
            menu.Bind(wx.EVT_MENU, self._create_node_view, item)
            self._widget_ids[item.GetId()] = widget

        self.AppendSubMenu(menu, 'New Node')

    # EVENT HANDLERS

    def _create_node_view(self, event):

        widget_id = event.GetId()
        widget = self._widget_ids[widget_id]
        self._canvas.create_node_view(widget)