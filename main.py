from Background import Background
from DockWindow import DockWindow
from Topbar import Topbar
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def main():
    bg = Background()
    bg.show_all()

    dock = DockWindow()
    dock.show_all()

    topbar = Topbar()
    topbar.show_all()

    Gtk.main()

if __name__ == "__main__":
    main()