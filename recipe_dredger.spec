# -*- mode: python ; coding: utf-8 -*-

import sys
from pathlib import Path

block_cipher = None

# Base directory
base_dir = Path('.')

# Collect all data files
datas = [
    ('templates', 'templates'),
    ('static', 'static'),
    ('data/*.txt', 'data'),
    ('data/config.example.json', 'data'),
    ('README*.md', '.'),
    ('GETTING_STARTED.md', '.'),
    ('SETUP.md', '.'),
]

# Hidden imports needed for Flask and dependencies
hiddenimports = [
    'flask',
    'jinja2',
    'werkzeug',
    'click',
    'itsdangerous',
    'blinker',
    'bs4',
    'lxml',
    'lxml.etree',
    'lxml._elementpath',
    'requests',
    'urllib3',
]

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Recipe_Dredger',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Keep console window for logs
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Add icon='icon.ico' if you have one
)
