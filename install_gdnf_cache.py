# -*- coding: utf-8 -*-
"""Instalando o Gdnf cache a partir do GitHub."""

import shutil
from configparser import ConfigParser
from os.path import expanduser, join, exists

config_file = './src/config/config.ini'
config = ConfigParser()
config.read(config_file)

app_name = config.get('DEFAULT', 'name')
description = config.get('DEFAULT', 'description')
version = config.get('DEFAULT', 'version')

home = expanduser('~')
src_path = 'src/'
dst_path = join(home, '.gdnf-cache')
icon_path = join(dst_path, 'data', 'icons', 'br.natorsc.Gdnfcache.png')
exec_path = join(dst_path, 'Application.py')
desktop_entry_path = join(home, '.local', 'share', 'applications', 'br.natorsc.Gdnfcache.desktop')

if exists(dst_path):
    shutil.rmtree(dst_path)
    shutil.copytree(src_path, dst_path)
else:
    shutil.copytree(src_path, dst_path)

# Criando arquivo `br.natorsc.Gdnfcache.desktop`.
with open(file='./src/data/br.natorsc.Gdnfcache.desktop.in', mode='r') as f:
    data = f.read()
    desktop_entry = data.format(version=version, name=app_name, comment=description,
                                path=dst_path, icon=icon_path, exec=exec_path)
    f.close()

# Salvando arquivo `br.natorsc.Gdnfcache.desktop`.
with open(file=desktop_entry_path, mode='w') as f:
    f.write(desktop_entry)
    f.close()

print('[!] Instalação realizada com sucesso [!]')
