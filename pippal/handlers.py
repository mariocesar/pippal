from gi.repository import Gtk


class MainWindowHandler:

    def create_environment_button_clicked(self, button):
        print('Create environment')

    def load_environment_button_clicked(self, button):
        print('Load environment')

    def preferences_button_clicked(self, button):
        print('Preferences')

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)