# -*- coding: utf-8 -*-
"""Remove o Gdnf cache."""

import shutil
from os import remove

from os.path import expanduser, join, exists

home = expanduser('~')
dst_path = join(home, '.gdnf-cache')
desktop_entry_path = join(home, '.local', 'share', 'applications', 'br.natorsc.Gdnfcache.desktop')

if exists(dst_path):
    shutil.rmtree(dst_path)
if exists(desktop_entry_path):
    remove(desktop_entry_path)
