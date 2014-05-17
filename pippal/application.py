import os

from gi.repository import Gio
from gi.repository import Gtk

from pippal.handlers import MainWindowHandler

class Pippal(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self, application_id="pippal.c1.com.bo",
            flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.license_type = Gtk.License.GPL_3_0

        self.builder = Gtk.Builder()
        self.builder.add_from_file(os.path.join(os.path.dirname(__file__), 'views.glade'))
        self.builder.connect_signals(MainWindowHandler())

    def do_activate(self):
        main_window = self.builder.get_object('main_window')
        main_window.show_all()

        self.add_window(main_window)