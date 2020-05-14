# -*- coding: utf-8 -*-
"""Janela de dialogo com informações do aplicativo."""
import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='./ui/DialogAbout.glade')
class DialogAbout(Gtk.AboutDialog):
    __gtype_name__ = 'DialogAbout'

    def __init__(self, parent):
        super().__init__(parent=parent)
        application = parent.application

        version = application.config.get('DEFAULT', 'version')
        self.set_version(version=version)

        self.show_all()
