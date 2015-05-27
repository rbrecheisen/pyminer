__author__ = 'Ralph'

import wx


class Canvas(wx.Panel):

    def __init__(self, parent, widgets):

        super(Canvas, self).__init__(parent)
        self._widgets = widgets
        self._nodes = []
        self._connections = []

        self.Bind(wx.EVT_PAINT, self._render)
        self.Bind(wx.EVT_RIGHT_UP, self._show_menu)
        self.Bind(wx.EVT_LEFT_DOWN, self._start_dragging)
        self.Bind(wx.EVT_LEFT_UP, self._stop_dragging)
        self.Bind(wx.EVT_MOTION, self._move)
        self.Bind(wx.EVT_LEFT_DCLICK, self._show_dialog)

    def create_node(self, widget):

        (x, y, width, height) = self.GetClientRect().Get()
        position = (x + width / 2, y + height / 2)
        self._nodes.append(Node(widget, position))
        self.Refresh()

    def delete_node(self, node):

        for connection in self._connections:
            if connection.has_node(node):
                self._connections.remove(connection)
        self._nodes.remove(node)
        self.Refresh()

    def _render(self, e):

        device = wx.PaintDC(self)

        for node in self._nodes:
            node.render(device)
        for connection in self._connections:
            connection.render(device)

    def _show_menu(self, e):

        position = e.GetPosition()
        menu = CanvasMenu(self, self._widgets)
        for node in self._nodes:
            if node.contains(position):
                menu = NodeMenu(self, node)
        self.PopupMenu(menu, e.GetPosition())

    def _start_dragging(self, e):

        position = e.GetPosition()
        for node in self._nodes:
            node.set_dragging(False)
            if node.is_input_port_selected(position):
                connection = Connection()
                connection.set_target(node.get_selected_port())
                self._connections.append(connection)
                break
            if node.is_output_port_selected(position):
                connection = Connection()
                connection.set_source(node.get_selected_port())
                self._connections.append(connection)
                break
            if node.contains(position):
                node.set_dragging(True)
                break

    def _stop_dragging(self, e):

        position = e.GetPosition()
        for node in self._nodes:
            node.set_dragging(False)
            if node.is_input_port_selected(position):
                for connection in self._connections:
                    if not connection.has_target():
                        connection.set_target(node.get_selected_port())
                        break
                continue
            if node.is_output_port_selected(position):
                for connection in self._connections:
                    if not connection.has_source():
                        connection.set_source(node.get_selected_port())
                        break
                continue
        for connection in self._connections:
            if connection.has_source() and connection.has_target():
                continue
            if not connection.has_source():
                self._connections.remove(connection)
                continue
            if not connection.has_target():
                self._connections.remove(connection)
        self.Refresh()

    def _move(self, e):

        position = e.GetPosition()
        for node in self._nodes:
            if node.is_dragging():
                node.set_position(position)
        for connection in self._connections:
            if connection.has_source() and connection.has_target():
                continue
            if not connection.has_source():
                connection.set_source_position(position)
                continue
            if not connection.has_target():
                connection.set_target_position(position)
                continue
        self.Refresh()

    def _show_dialog(self):
        pass


class CanvasMenu(wx.Menu):

    def __init__(self, canvas, widgets):

        super(CanvasMenu, self).__init__()
        self._canvas = canvas
        self._widget_ids = {}
        menu = wx.Menu()

        for widget in widgets:
            item = wx.MenuItem(self, wx.NewId(), widget.get_name())
            menu.AppendItem(item)
            menu.Bind(wx.EVT_MENU, self._create_node, item)
            self._widget_ids[item.GetId()] = widget

        self.AppendSubMenu(menu, 'New Node')

    def _create_node(self, e):

        widget_id = e.GetId()
        widget = self._widget_ids[widget_id]
        self._canvas.create_node(widget)


class Port(object):

    def __init__(self, port):

        super(Port, self).__init__()
        self._port = port
        self._width = 10
        self._height = 10
        self._position = (0, 0)

    def render(self, device):

        device.SetPen(wx.Pen(wx.BLACK))
        device.SetBrush(wx.Brush(wx.BLUE))
        device.DrawRectangle(self._position[0], self._position[1], self._width, self._height)

    def get_position(self):

        return self._position

    def set_position(self, position):

        self._position = position

    def get_port(self):

        return self._port

    def get_node(self):

        return self.get_port().get_node()

    def get_name(self):

        return self.get_port().get_name()

    def contains(self, position):

        x = position[0]
        y = position[1]
        if self._position[0] < x < self._position[0] + self._width and self._position[1] < y < self._position[1] + self._height:
            return True
        return False


class Node(object):

    def __init__(self, widget, position):

        super(Node, self).__init__()
        self._position = position
        self._widget = widget
        self._width = 50
        self._height = 50
        self._dragging = False
        self._selected_port = None

        self._input_ports = []
        for input_port in self.get_node().get_input_ports():
            self._input_ports.append(Port(input_port))

        self._output_ports = []
        for output_port in self.get_node().get_output_ports():
            self._output_ports.append(Port(output_port))

    def render(self, device):

        device.SetPen(wx.Pen(wx.BLACK))
        device.SetBrush(wx.Brush(wx.RED))
        device.DrawRectangle(self._position[0], self._position[1], self._width, self._height)
        device.DrawText(self._widget.get_name(), self._position[0], self._position[1] + self._height + 5)

        for i in range(len(self._input_ports)):
            input_port = self._input_ports[i]
            input_port.set_position((self._position[0] - 10, self._position[1] + i * 20))
            input_port.render(device)

        for i in range(len(self._output_ports)):
            output_port = self._output_ports[i]
            output_port.set_position((self._position[0] + self._width - 1, self._position[1] + i * 20))
            output_port.render(device)

    def get_node(self):

        return self.get_widget().get_node()

    def get_widget(self):

        return self._widget

    def get_position(self):

        return self._position

    def set_position(self, position):

        self._position = (position[0] - self._width / 2, position[1] - self._height / 2)

    def is_input_port_selected(self, position):

        for input_port in self._input_ports:
            if input_port.contains(position):
                self._selected_port = input_port
                return True
        return False

    def is_output_port_selected(self, position):

        for output_port in self._output_ports:
            if output_port.contains(position):
                self._selected_port = output_port
                return True
        return False

    def get_selected_port(self):

        return self._selected_port

    def contains(self, position):

        x = position[0]
        y = position[1]
        if self._position[0] < x < self._position[0] + self._width and self._position[1] < y < self._position[1] + self._height:
            return True
        return False

    def is_dragging(self):

        return self._dragging

    def set_dragging(self, dragging):

        self._dragging = dragging


class NodeMenu(wx.Menu):

    def __init__(self, canvas, node):

        super(NodeMenu, self).__init__()
        self._canvas = canvas
        self._node = node
        item = wx.MenuItem(self, wx.NewId(), 'Delete Node')
        self.AppendItem(item)
        self.Bind(wx.EVT_MENU, self._delete_node, item)

    def _delete_node(self, e):

        self._canvas.delete_node(self._node)


class Connection(object):

    def __init__(self):

        super(Connection, self).__init__()
        self._source = None
        self._target = None
        self._source_position = (0, 0)
        self._target_position = (0, 0)

    def render(self, device):

        device.SetPen(wx.Pen(wx.BLACK))

        (x1, y1) = self._source_position
        if self.has_source():
            (x1, y1) = self.get_source().get_position()

        (x2, y2) = self._target_position
        if self.has_target():
            (x2, y2) = self.get_target().get_position()

        device.DrawLine(x1, y1, x2, y2)

    def get_source(self):

        return self._source

    def set_source(self, source):

        self._source = source
        self._source_position = source.get_position()

    def set_source_position(self, position):

        if self._source is None:
            self._source_position = position

    def has_source(self):

        return self.get_source() is not None

    def get_target(self):

        return self._target

    def set_target(self, target):

        self._target = target
        self._target_position = target.get_position()

    def set_target_position(self, position):

        if self._target is None:
            self._target_position = position

    def has_target(self):

        return self.get_target() is not None

    def has_node(self, node):

        if self.has_source() and self.get_source().get_node() is node.get_node():
            return True
        if self.has_target() and self.get_target().get_node() is node.get_node():
            return True
        return False


class ConnectionMenu(object):
    pass