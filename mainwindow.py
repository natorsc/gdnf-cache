# -*- coding: utf-8 -*-
"""gdnf-cache."""
import threading

import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk, GdkPixbuf

from scripts.ConnectSQLite import ConnectDB
from scripts.dnf_utilits import get_dnf_metadata


class DialogPackageInfo(Gtk.Dialog):
    def __init__(self, parent, row_data):
        super().__init__(parent=parent)
        # Dados
        tree_selection = row_data.get_selection()
        liststore, treeiter = tree_selection.get_selected()

        arch = liststore[treeiter][0]
        description = liststore[treeiter][1]
        license = liststore[treeiter][2]
        pkg_name = liststore[treeiter][3]
        reponame = liststore[treeiter][4]
        summary = liststore[treeiter][5]
        version = liststore[treeiter][6]

        self.set_title(title=pkg_name)
        self.set_modal(modal=True)
        self.add_button(button_text='OK', response_id=Gtk.ResponseType.OK)

        vbox = self.get_content_area()
        vbox.set_spacing(spacing=12)
        vbox.set_border_width(12)

        str_pkg = f'<span size="medium"><b>Pacote</b></span>: {pkg_name}.'
        lbl_pkg_name = Gtk.Label.new(str=str_pkg)
        lbl_pkg_name.set_use_markup(setting=True)
        lbl_pkg_name.set_xalign(xalign=0)
        vbox.add(widget=lbl_pkg_name)

        str_ver = f'<span size="medium"><b>Versão</b></span>: {version}.'
        lbl_version = Gtk.Label.new(str=str_ver)
        lbl_version.set_use_markup(setting=True)
        lbl_version.set_xalign(xalign=0)
        vbox.add(widget=lbl_version)

        str_arc = f'<span size="medium"><b>Arquitetura(s)</b></span>: {arch.split(",")}.'
        lbl_arch = Gtk.Label.new(str=str_arc)
        lbl_arch.set_use_markup(setting=True)
        lbl_arch.set_xalign(xalign=0)
        vbox.add(widget=lbl_arch)

        str_sum = f'<span size="medium"><b>Sumário</b></span>: {summary}.'
        lbl_summary = Gtk.Label.new(str=str_sum)
        lbl_summary.set_use_markup(setting=True)
        lbl_summary.set_xalign(xalign=0)
        vbox.add(widget=lbl_summary)

        str_rep = f'<span size="medium"><b>Repositório</b></span>: {reponame.split(",")}.'
        lbl_reponame = Gtk.Label.new(str=str_rep)
        lbl_reponame.set_use_markup(setting=True)
        lbl_reponame.set_xalign(xalign=0)
        vbox.add(widget=lbl_reponame)

        str_lic = f'<span size="medium"><b>Licença</b></span>: {license}.'
        lbl_license = Gtk.Label.new(str=str_lic)
        lbl_license.set_use_markup(setting=True)
        lbl_license.set_xalign(xalign=0)
        vbox.add(widget=lbl_license)

        str_desc = f'<span size="medium"><b>Descrição</b></span>:\n\n{description}'
        lbl_description = Gtk.Label.new(str=str_desc)
        lbl_description.set_use_markup(setting=True)
        lbl_description.set_xalign(xalign=0)
        vbox.add(widget=lbl_description)

        self.show_all()


class Handler:
    logo = GdkPixbuf.Pixbuf.new_from_file(filename='./data/icons/icon.png')

    def __init__(self):
        self.db = ConnectDB(dbpath='./data/db.sqlite3')

        self.btn_update_cache = builder.get_object(name='btn-update-cache')
        self.revealer_search = builder.get_object(name='revealer-search')
        self.liststore = builder.get_object(name='liststore')

        self.settings = Gtk.Settings.get_default()

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

    def start_thread_btn_update_cache(self, widget):
        """Processo é executado em outra thred.
        
        Isso evita o bloqueio do loop da interface.

        :param widget: (obj) Widget que disparou o evento.
        """
        widget.set_sensitive(sensitive=False)
        thread = threading.Thread(target=self.update_dnf_cache, args=(widget,))
        thread.daemon = True
        thread.start()

    def on_double_click_row(self, TreeView, i, TreeViewColumn):
        dialog_info = DialogPackageInfo(parent=win, row_data=TreeView)
        dialog_info.run()
        dialog_info.destroy()

    def enable_disable_dark_mode(self, widget, state):
        if widget.get_active():
            self.settings.set_property('gtk-application-prefer-dark-theme', True)
        else:
            self.settings.set_property('gtk-application-prefer-dark-theme', False)

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
