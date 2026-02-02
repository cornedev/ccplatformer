#!/bin/bash
set -e
cd "$(dirname "$0")"
python -m PyInstaller --onefile --windowed --icon=gfx/icon.ico --name ccplatformer game.py
cp -r gfx dist/gfx
cp -r sfx dist/sfx
