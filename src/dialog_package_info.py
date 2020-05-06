# -*- coding: utf-8 -*-
"""Janela de dialogo que exibi as informações do pacote selecionado."""
import gi

gi.require_version(namespace='Gtk', version='3.0')
from gi.repository import Gtk


def package_info_dialog(TreeView, i, TreeViewColumn):
    tree_selection = TreeView.get_selection()
    liststore, treeiter = tree_selection.get_selected()

    arch = liststore[treeiter][0]
    description = liststore[treeiter][1]
    license = liststore[treeiter][2]
    pkg_name = liststore[treeiter][3]
    reponame = liststore[treeiter][4]
    summary = liststore[treeiter][5]
    version = liststore[treeiter][6]

    builder = Gtk.Builder.new()
    builder.add_from_file(filename='./ui/dialog-pkg-info.glade')
    pkg_info_dialog = builder.get_object(name='dialog-pkg-info')
    pkg_info_dialog.set_title(title=pkg_name)

    str_pkg = f'<span size="medium"><b>Pacote</b></span>: {pkg_name}.'
    lbl_pkg_name = builder.get_object(name='lbl-pkg-name')
    lbl_pkg_name.set_markup(str=str_pkg)

    str_ver = f'<span size="medium"><b>Versão</b></span>: {version}.'
    lbl_version = builder.get_object(name='lbl-version')
    lbl_version.set_markup(str=str_ver)

    str_arc = f'<span size="medium"><b>Arquitetura(s)</b></span>: {arch.split(",")}.'
    lbl_arch = builder.get_object(name='lbl-arch')
    lbl_arch.set_markup(str=str_arc)

    str_sum = f'<span size="medium"><b>Sumário</b></span>: {summary}.'
    lbl_summary = builder.get_object(name='lbl-summary')
    lbl_summary.set_markup(str=str_sum)

    str_rep = f'<span size="medium"><b>Repositório</b></span>: {reponame.split(",")}.'
    lbl_reponame = builder.get_object(name='lbl-reponame')
    lbl_reponame.set_markup(str=str_rep)

    str_lic = f'<span size="medium"><b>Licença</b></span>: {license}.'
    lbl_license = builder.get_object(name='lbl-license')
    lbl_license.set_markup(str=str_lic)

    str_desc = f'<span size="medium"><b>Descrição</b></span>:\n\n{description}'
    lbl_description = builder.get_object(name='lbl-description')
    lbl_description.set_markup(str=str_desc)

    pkg_info_dialog.show()
