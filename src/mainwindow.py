# -*- coding: utf-8 -*-
"""gdnf-cache."""
import threading

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, GdkPixbuf

from scripts.ConnectSQLite import ConnectDB
from scripts.dnf_utilits import get_dnf_metadata
from dialog_package_info import package_info_dialog
from dialog_about import about_dialog


class Handler:
    def __init__(self):
        self.db = ConnectDB(dbpath='./data/db.sqlite3')

        self.settings = Gtk.Settings.get_default()

        self.btn_update_cache = builder.get_object(name='btn-update-cache')
        self.revealer_search = builder.get_object(name='revealer-search')
        self.liststore = builder.get_object(name='liststore')

        switch_dark_mode = builder.get_object(name='switch-dark-mode')
        switch_dark_mode.connect('notify::active', self.enable_disable_dark_mode)

    def show_hide_search(self, widget):
        show = self.revealer_search.get_reveal_child()
        if show:
            self.revealer_search.set_reveal_child(reveal_child=False)
        else:
            self.revealer_search.set_reveal_child(reveal_child=True)

    def search(self, widget):
        entry_text = widget.get_text()
        if entry_text:
            rows = self.db.get_package_by_name(name=entry_text)
            self.liststore.clear()
            for row in rows:
                self.liststore.append(row=row)
        else:
            self.liststore.clear()

    def update_dnf_cache(self, widget):
        self.db.drop_table(table='available')
        self.db.create_table()
        data = get_dnf_metadata()
        self.db.insert_dnf_metadata(data=data)
        widget.set_sensitive(sensitive=True)

    def enable_disable_dark_mode(self, widget, state):
        if widget.get_active():
            self.settings.set_property('gtk-application-prefer-dark-theme', True)
        else:
            self.settings.set_property('gtk-application-prefer-dark-theme', False)

    def start_thread_btn_update_cache(self, widget):
        """Processo é executado em outra thred.
        
        Isso evita o bloqueio do loop da interface.

        :param widget: (obj) Widget que disparou o evento.
        """
        widget.set_sensitive(sensitive=False)
        thread = threading.Thread(target=self.update_dnf_cache, args=(widget,))
        thread.daemon = True
        thread.start()

    @staticmethod
    def open_package_info_dialog(TreeView, i, TreeViewColumn):
        package_info_dialog(TreeView, i, TreeViewColumn)

    @staticmethod
    def open_about_dialog(widget):
        about_dialog()


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./ui/mainwindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
