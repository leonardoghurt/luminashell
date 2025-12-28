import gi
gi.require_version("Gtk", "3.0")
gi.require_version("GtkLayerShell", "0.1")
from gi.repository import Gtk, GtkLayerShell, Gdk, GLib
from DockView import DockView

class DockWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        GtkLayerShell.init_for_window(self)
        GtkLayerShell.set_layer(self, GtkLayerShell.Layer.TOP)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.BOTTOM, True)
        GtkLayerShell.set_exclusive_zone(self, 0)
        GtkLayerShell.set_margin(self, GtkLayerShell.Edge.BOTTOM, 0)
        self.set_decorated(False)
        self.set_resizable(False)

        self.dockview = DockView()
        self.add(self.dockview)
        self.show_all()
        self.hide()

        self.hide_timeout_id = None
        GLib.timeout_add(50, self.check_mouse_position)

    def check_mouse_position(self):
        display = Gdk.Display.get_default()
        seat = display.get_default_seat()
        pointer = seat.get_pointer()
        _, x, y = pointer.get_position()

        screen_height = self.get_screen().get_height()
        win_x, win_y = self.get_position()
        win_width, win_height = self.get_size()

        near_bottom = y >= screen_height - 5
        over_window = win_x <= x <= win_x + win_width and win_y <= y <= win_y + win_height

        if over_window or near_bottom:
            if self.hide_timeout_id:
                GLib.source_remove(self.hide_timeout_id)
                self.hide_timeout_id = None
            if not self.is_visible():
                self.show_all()
        else:
            if self.is_visible() and self.hide_timeout_id is None:
                self.hide_timeout_id = GLib.timeout_add(400, self.hide_dock)

        return True

    def hide_dock(self):
        self.hide()
        self.hide_timeout_id = None
        return False

win = DockWindow()