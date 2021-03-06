# -*- coding: utf-8 -*-
"""gdnf-cache."""
from threading import Thread

import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

from DialogAbout import DialogAbout
from DialogPkgInfo import DialogPkgInfo
from scripts.dnf_utilits import create_dnf_cache, update_dnf_cache


@Gtk.Template(filename='./ui/MainWindow.glade')
class MainWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'MainWindow'

    btn_update_cache = Gtk.Template.Child(name='btn-update-cache')
    btn_open_search = Gtk.Template.Child(name='btn-open-search')
    revealer_search = Gtk.Template.Child(name='revealer-search')
    liststore = Gtk.Template.Child(name='liststore')
    switch_dark_mode = Gtk.Template.Child(name='switch-dark-mode')
    searchentry = Gtk.Template.Child(name='searchentry')

    radio_button_10 = Gtk.Template.Child(name='radio-button-10')
    radio_button_30 = Gtk.Template.Child(name='radio-button-30')
    radio_button_50 = Gtk.Template.Child(name='radio-button-50')
    radio_button_all = Gtk.Template.Child(name='radio-button-all')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.application = kwargs['application']

        self.limit = self.application.limit

        radio_buttons = {
            '10': self.radio_button_10,
            '30': self.radio_button_30,
            '50': self.radio_button_50,
            '-1': self.radio_button_all,
        }
        # Definindo qual radio button inicia ativo com base no ultimo valor salvo
        radio_buttons[self.limit].set_active(is_active=True)

        self.switch_dark_mode.set_state(state=self.application.darkmode)
        self.switch_dark_mode.connect('notify::active', self.enable_disable_dark_mode)

        if not self.application.db.table_exists(table='available'):
            self.thread_create_dnf_cache()

    def enable_disable_dark_mode(self, widget, state):
        switch_state = widget.get_active()
        if switch_state:
            self.application.settings.set_property('gtk-application-prefer-dark-theme', switch_state)
            self.application.config.set('DEFAULT', 'darkmode', str(switch_state))
        else:
            self.application.settings.set_property('gtk-application-prefer-dark-theme', switch_state)
            self.application.config.set('DEFAULT', 'darkmode', str(switch_state))

    def thread_create_dnf_cache(self):
        self.btn_update_cache.set_sensitive(sensitive=False)
        self.btn_open_search.set_sensitive(sensitive=False)
        thread = Thread(
            target=create_dnf_cache,
            args=(self.btn_update_cache, self.btn_open_search),
        )
        thread.start()

    @Gtk.Template.Callback()
    def on_radiobutton_toggled(self, widget):
        value = widget.get_label().split(' ')
        if len(value) < 2:
            self.limit = -1
        else:
            self.limit = value[-1]
        if widget.get_active():
            self.search(widget=self.searchentry)
        else:
            pass
        self.application.config.set('DEFAULT', 'limit', str(self.limit))

    @Gtk.Template.Callback()
    def thead_update_cache_clicked(self, widget):
        self.btn_open_search.set_sensitive(sensitive=False)
        widget.set_sensitive(sensitive=False)
        thread = Thread(
            target=update_dnf_cache,
            args=(widget, self.btn_open_search),
        )
        thread.start()

    @Gtk.Template.Callback()
    def open_about_dialog(self, widget):
        DialogAbout(parent=self)

    @Gtk.Template.Callback()
    def open_pkg_info_dialog(self, TreeView, i, TreeViewColumn):
        DialogPkgInfo(parent=self, TreeView=TreeView, i=i, TreeViewColumn=TreeViewColumn)

    @Gtk.Template.Callback()
    def search(self, widget):
        entry_text = widget.get_text()
        if entry_text:
            rows = self.application.db.get_packages_by_name(name=entry_text, limit=self.limit)
            self.liststore.clear()
            for row in rows:
                self.liststore.append(row=row)
        else:
            self.liststore.clear()

    @Gtk.Template.Callback()
    def show_hide_search(self, widget):
        if self.revealer_search.get_reveal_child():
            self.revealer_search.set_reveal_child(reveal_child=False)
        else:
            self.revealer_search.set_reveal_child(reveal_child=True)


if __name__ == '__main__':
    pass
