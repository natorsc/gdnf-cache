#!/usr/bin/env bash
pyinstaller --noconfirm --log-level=WARN \
--windowed \
--name="gdnf-cache" \
--add-data="./data:data" \
--add-data="./scripts:scripts" \
--add-data="./ui:ui" \
--exclude-module="tkinter" \
--upx-dir=/usr/local/share/ \
mainwindow.py
