# -*- coding: utf-8 -*-
"""gdnf-cache."""
import threading

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, GdkPixbuf

from scripts.ConnectSQLite import ConnectDB
from scripts.dnf_utilits import get_dnf_metadata


class Handler:
    logo = GdkPixbuf.Pixbuf.new_from_file(filename='./data/icons/icon.png')

    def __init__(self):
        self.db = ConnectDB(dbpath='./data/db.sqlite3')

        self.btn_update_cache = builder.get_object(name='btn-update-cache')
        self.revealer_search = builder.get_object(name='revealer-search')
        self.liststore = builder.get_object(name='liststore')

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

    def start_thread_btn_update_cache(self, widget):
        widget.set_sensitive(sensitive=False)
        thread = threading.Thread(target=self.update_dnf_cache, args=(widget,))
        thread.daemon = True
        thread.start()

    def open_dialog_about(self, widget):
        about = Gtk.AboutDialog.new()
        about.set_logo(logo=self.logo)
        about.set_authors(authors=('Renato Cruz',))
        about.set_comments(
            comments='Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                     'sed do eiusmod tempor incididunt ut labore et dolore '
                     'magna aliqua.'
        )
        about.set_website(website='https://github.com/natorsc/gui-python-gtk')
        about.run()
        about.destroy()


if __name__ == '__main__':
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='mainwindow.glade')
    builder.connect_signals(obj_or_map=Handler())

    win = builder.get_object(name='MainWindow')
    win.connect('destroy', Gtk.main_quit)
    win.show_all()
    Gtk.main()
