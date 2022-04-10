#!/usr/bin/env python3

import os
import subprocess
import platform

if platform.processor() == "arm":
    homebrewdir = os.path.join('/', 'opt', 'homebrew')
else:
    homebrewdir = os.path.join('/', 'usr', 'local')


schemadir = os.path.join(homebrewdir, 'share', 'glib-2.0', 'schemas');
iconsdir = os.path.join(homebrewdir, 'share', 'icons');
themesdir = os.path.join(homebrewdir, 'share', 'themes');

os.makedirs(os.getenv("HOME") + '/.config/gtk-3.0/', exist_ok=True)

os.system('cp ../schema/* ' + schemadir)
os.system('cp -r ../icons/elementary ' + iconsdir + '/elementary')
os.system('cp -r ../themes/io.elementary.strawberry ' + themesdir + '/io.elementary.strawberry')
os.system('cp ../meson/settings.ini ' + '~/.config/gtk-3.0/settings.ini')

os.system('cp ../build/src/io.elementary.code ' + '../application/Code.app/Contents/MacOS/io.elementary.code')
os.system('cp -r ../application/Code.app ' + '/Applications/Code.app')

subprocess.call(['glib-compile-schemas', schemadir])
subprocess.call('gtk3-update-icon-cache')
