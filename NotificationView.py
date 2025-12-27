import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GtkLayerShell, GLib
from Screen import Screen
from time import sleep

screen_object = Screen(0)

class NotificationView(Gtk.Window):
    def __init__(self, notification_text):
        super().__init__(title="Notification")

        GtkLayerShell.init_for_window(self)
        GtkLayerShell.set_layer(self, GtkLayerShell.Layer.OVERLAY)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.TOP, True)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.RIGHT, True)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.LEFT, True)

        self.set_default_size(screen_object.width(), screen_object.height() // 10)

        self.set_decorated(False)
        self.set_resizable(False)

        style_provider = Gtk.CssProvider()
        style_provider.load_from_path("css/notificationStylesheet.css")
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(box)

        label = Gtk.Label(label=notification_text)
        label.set_halign(Gtk.Align.CENTER)  # Centra horizontalmente
        label.set_valign(Gtk.Align.CENTER)
        box.pack_start(label, True, True, 0)
        box.set_halign(Gtk.Align.CENTER)
        box.set_valign(Gtk.Align.CENTER)

        self.show_all()

        GLib.timeout_add(5000, self.destroy)

        Gtk.main()
        