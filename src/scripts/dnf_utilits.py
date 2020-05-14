# -*- coding: utf-8 -*-
"""Arquivo com os métodos e funções que irão manipular o `dnf`.

O pacote `dnf` não funciona em ambientes virtuais, deve-se utilizar o
interpretador Python do sistema!

Verificar em qual versão do Python o pacote `python3-dnf` está instalado.
"""
from configparser import ConfigParser

from dnf import Base
from scripts.ConnectSQLite import ConnectDB

config_file = './config/config.ini'
config = ConfigParser()
config.read(config_file)


def database():
    dbpath = config.get('DATABASE', 'dbpath')
    return ConnectDB(dbpath=dbpath)


def dnf_base():
    base = Base()
    base.read_all_repos()
    base.fill_sack()
    base.sack.query()
    return base.sack.query()


def update_dnf_available(base):
    db = database()
    db.drop_table(table='available')
    db.create_table_available()

    q_available = base.available().latest()
    available_packages = q_available.run()
    available = [(pkg.arch, pkg.description, pkg.license, pkg.name, pkg.release,
                  pkg.reponame, pkg.summary, pkg.version) for pkg in available_packages]
    db.insert_dnf_available(data=available)


def update_dnf_installed(base):
    db = database()
    db.drop_table(table='installed')
    db.create_table_installed()

    q_installed = base.installed()
    installed_packages = q_installed.run()
    installed = [(pkg.name, pkg.installed,) for pkg in installed_packages]
    db.insert_dnf_installed(data=installed)


def update_dnf_cache(widget, btn_open_search):
    base = dnf_base()
    update_dnf_available(base=base)
    update_dnf_installed(base=base)
    btn_open_search.set_sensitive(sensitive=True)
    widget.set_sensitive(sensitive=True)


def create_dnf_available(base):
    db = database()
    db.create_table_available()

    q_available = base.available().latest()
    available_packages = q_available.run()
    available = [(pkg.arch, pkg.description, pkg.license, pkg.name, pkg.release,
                  pkg.reponame, pkg.summary, pkg.version) for pkg in available_packages]
    db.insert_dnf_available(data=available)


def create_dnf_installed(base):
    db = database()
    db.create_table_installed()

    q_installed = base.installed()
    installed_packages = q_installed.run()
    installed = [(pkg.name, pkg.installed,) for pkg in installed_packages]
    db.insert_dnf_installed(data=installed)


def create_dnf_cache(btn_update_cache, btn_open_search):
    base = dnf_base()
    create_dnf_available(base=base)
    create_dnf_installed(base=base)
    btn_update_cache.set_sensitive(sensitive=True)
    btn_open_search.set_sensitive(sensitive=True)


if __name__ == '__main__':
    pass
