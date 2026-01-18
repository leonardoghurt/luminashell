import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf
import os
import sys
from subprocess import Popen

luminashell = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if luminashell not in sys.path:
    sys.path.insert(0, luminashell)

import config
from Launchpad import Launchpad

launchpad_object = Launchpad()


class View(Gtk.Window):
    def __init__(self):
        super().__init__(title="Launchpad")

        self.set_border_width(10)
        self.set_default_size(400, 300)

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

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.box.set_name("mainBox")
        self.add(self.box)

        title = Gtk.Label(label="Launchpad")
        self.box.pack_start(title, False, False, 0)

        self.grid = Gtk.Grid()
        self.grid.set_row_spacing(10)
        self.grid.set_column_spacing(10)
        self.box.pack_start(self.grid, True, True, 0)

        col = 0
        row = 0
        max_cols = 5

        apps = launchpad_object.builddict()

        for item, data in apps.items():
            path = data.get("path")
            icon = data.get("icon")

            if not path or not icon:
                continue
            if not os.path.exists(icon):
                print("Icon not found")
                continue
            btn = Gtk.Button()
            btn.set_name("launchpad-button")

            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(
                icon, config.icon_size, config.icon_size
            )
            image = Gtk.Image.new_from_pixbuf(pixbuf)
            btn.set_image(image)

            btn.connect("clicked", self.launch_app, path)

            self.grid.attach(btn, col, row, 1, 1)

            col += 1
            if col >= max_cols:
                col = 0
                row += 1


        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def launch_app(self, button, command):
        Popen(command.split())


View()
Gtk.main()