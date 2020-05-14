# -*- coding: utf-8 -*-
"""Gtk.Application.

- startup: Configura o aplicativo quando é iniciado pela primeira vez.
- shutdown: Eecuta tarefas quando o aplicativo é desligado.
- activate: Mostra a janela principal do aplicativo (como um novo documento).
- open: Abre arquivos e mostra-os em uma nova janela.
"""
from configparser import ConfigParser

import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio

from scripts.ConnectSQLite import ConnectDB

from MainWindow import MainWindow


class Application(Gtk.Application):
    config_file = './config/config.ini'
    config = ConfigParser()
    config.read(config_file)

    darkmode = config.getboolean('DEFAULT', 'darkmode')
    dbpath = config.get('DATABASE', 'dbpath')

    settings = Gtk.Settings.get_default()

    def __init__(self):
        super().__init__(application_id='br.natorsc.GdnfCache',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        self.db = ConnectDB(dbpath=self.dbpath)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)
        if self.darkmode:
            self.settings.set_property('gtk-application-prefer-dark-theme', self.darkmode)

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)
        self.save_darkmode_status()

    def save_darkmode_status(self):
        with open(file=self.config_file, mode='w') as f:
            self.config.write(f)
            f.close()


if __name__ == '__main__':
    import sys

    app = Application()
    app.run(sys.argv)
