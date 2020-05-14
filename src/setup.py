# -*- coding: utf-8 -*-
"""Gerando executável com Cx_Freeze.

sudo dnf install rpm-build rpmdevtools install redhat-rpm-config  gcc make

python3 setup.py build
python3 setup.py bdist_rpm
"""
from configparser import ConfigParser

from cx_Freeze import Executable, setup

config_file = './config/config.ini'
config = ConfigParser()
config.read(config_file)

version = config.get('DEFAULT', 'version')

base = None

build_exe_options = {
    'excludes': ['tkinter'],
    'include_files': ['config', 'data', 'scripts', 'ui', 'Application.py',
                      'DialogAbout.py', 'DialogPkgInfo.py'],
    'packages': ['gi', 'sqlite3', 'dnf', 'gpg'],
}

setup(
    name='br.natorsc.Gdnfcache',
    version=version,
    author='Renato Cruz',
    author_email='natorsc@gmail.com',
    description='Ferramenta de busca e pesquisa dos pacotes do Fedora.',
    options={'build_exe': build_exe_options},
    executables=[
        Executable(
            script='Application.py',
            targetName="Gdnfcache",
            base=base,
            icon='./data/icons/br.natorsc.Gdnfcache.ico',
        ),
    ],
)
