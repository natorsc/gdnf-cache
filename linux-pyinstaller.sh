#!/usr/bin/env bash
pyinstaller --noconfirm --log-level=WARN \
--windowed \
--name="GdnfCache" \
--add-data="./src:." \
--exclude-module="tkinter" \
--upx-dir=/usr/local/share/ \
./src/Application.py
