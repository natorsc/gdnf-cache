# -*- coding: utf-8 -*-
"""Janela de dialogo sobre."""
import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


def about_dialog():
    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./ui/dialog-about.glade')
    about_dialog = builder.get_object(name='dialog-about')
    about_dialog.show()
