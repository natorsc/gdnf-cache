# -*- coding: utf-8 -*-
"""Janela de dialogo que exibi as informações do pacote selecionado."""
import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


@Gtk.Template(filename='./ui/DialogPkgInfo.glade')
class DialogPkgInfo(Gtk.Dialog):
    __gtype_name__ = 'DialogPkgInfo'

    lbl_pkg_name = Gtk.Template.Child(name='lbl-pkg-name')
    lbl_version = Gtk.Template.Child(name='lbl-version')
    lbl_arch = Gtk.Template.Child(name='lbl-arch')
    lbl_summary = Gtk.Template.Child(name='lbl-summary')
    lbl_release = Gtk.Template.Child(name='lbl-release')
    lbl_reponame = Gtk.Template.Child(name='lbl-reponame')
    lbl_license = Gtk.Template.Child(name='lbl-license')
    lbl_installed = Gtk.Template.Child(name='lbl-installed')
    lbl_description = Gtk.Template.Child(name='lbl-description')

    def __init__(self, parent, TreeView, i, TreeViewColumn):
        super().__init__(parent=parent)
        application = parent.application

        tree_selection = TreeView.get_selection()
        liststore, treeiter = tree_selection.get_selected()
        arch = liststore[treeiter][0]
        description = liststore[treeiter][1]
        license = liststore[treeiter][2]
        pkg_name = liststore[treeiter][3]
        release = liststore[treeiter][4]
        reponame = liststore[treeiter][5]
        summary = liststore[treeiter][6]
        version = liststore[treeiter][7]

        installed = application.db.get_package_installed(name=pkg_name)

        self.set_title(title=pkg_name)

        str_pkg = f'<span size="medium"><b>Pacote</b></span>: {pkg_name}.'
        self.lbl_pkg_name.set_markup(str=str_pkg)

        str_ver = f'<span size="medium"><b>Versão</b></span>: {version}.'
        self.lbl_version.set_markup(str=str_ver)

        str_arc = f'<span size="medium"><b>Arquitetura(s)</b></span>: {", ".join(arch.split(","))}.'
        self.lbl_arch.set_markup(str=str_arc)

        str_sum = f'<span size="medium"><b>Sumário</b></span>: {summary}.'
        self.lbl_summary.set_markup(str=str_sum)

        str_rep = f'<span size="medium"><b>Repositório(s)</b></span>: {", ".join(reponame.split(","))}.'
        self.lbl_reponame.set_markup(str=str_rep)

        str_lic = f'<span size="medium"><b>Licença</b></span>: {license}.'
        self.lbl_license.set_markup(str=str_lic)

        str_rel = f'<span size="medium"><b>lançamento</b></span>: {release}.'
        self.lbl_release.set_markup(str=str_rel)

        ins = 'Sim' if installed else 'Não'
        str_ins = f'<span size="medium"><b>Instalado</b></span>: {ins}.'
        self.lbl_installed.set_markup(str=str_ins)

        str_desc = f'<span size="medium"><b>Descrição</b></span>:\n\n{description}'
        self.lbl_description.set_markup(str=str_desc)

        self.show_all()
