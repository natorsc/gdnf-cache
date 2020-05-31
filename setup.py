# -*- coding: utf-8 -*-
"""Gerando executável com Cx_Freeze.

sudo dnf install rpm-build rpmdevtools install redhat-rpm-config  gcc make

python3 setup.py build
python3 setup.py bdist_rpm
"""
from configparser import ConfigParser

from cx_Freeze import Executable, setup

config_file = './src/config/config.ini'
config = ConfigParser()
config.read(config_file)

app_name = config.get('DEFAULT', 'app_name')
app_id = config.get('DEFAULT', 'app_id')
description = config.get('DEFAULT', 'description')
author = config.get('DEFAULT', 'author')
author_email = config.get('DEFAULT', 'author_email')
version = config.get('DEFAULT', 'version')

base = None

build_exe_options = {
    'excludes': ['tkinter'],
    'include_files': [
        'src/config', 'src/data', 'src/scripts', 'src/ui', 'src/Application.py',
        'src/DialogAbout.py', 'src/DialogPkgInfo.py', 'src/MainWindow.py'
    ],
    'packages': ['gi', 'sqlite3', 'dnf', 'gpg'],
}

setup(
    name=app_name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    options={'build_exe': build_exe_options},
    executables=[
        Executable(
            script='./src/Application.py',
            targetName='GdnfCache',
            base=base,
            icon='./src/data/icons/br.natorsc.Gdnfcache.ico',
        ),
    ],
)
