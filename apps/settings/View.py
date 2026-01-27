import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
gi.require_version("GtkLayerShell", "0.1")
from gi.repository import Gtk, Gdk, GdkPixbuf, GtkLayerShell
import os
import sys
from subprocess import Popen
luminashell = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if luminashell not in sys.path:
    sys.path.insert(0, luminashell)
import config
from Config import Config

class View(Gtk.Window):
    def __init__(self):
        super().__init__(title="Settings")

        self.set_border_width(10)
        self.set_default_size(600, 400)
        self.set_resizable(False)
        self.set_app_paintable(True)
        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual:
            self.set_visual(visual)

        css_provider = Gtk.CssProvider()
        css_provider.load_from_path("css/transparentStylesheet.css")
        Gtk.StyleContext.add_provider_for_screen(
            screen,
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        self.box = Gtk.ScrolledWindow()
        self.box.set_policy(
            Gtk.PolicyType.AUTOMATIC,
            Gtk.PolicyType.AUTOMATIC
        )
        self.add(self.box)
        self.box.set_name("mainBox")
        
        self.title = Gtk.Label(label="Settings")
        
        self.box.add(self.title)

        self.show_all()

View()
Gtk.main()