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

os.system('cp ../schema/* ' + schemadir)
os.system('cp -r ../icons/elementary ' + iconsdir + '/elementary')
os.system('cp ../meson/settings.ini ' + '~/.config/gtk-3.0/settings.ini')

os.system('cp ../build/src/io.elementary.code ' + '../application/Code.app/Contents/MacOS/io.elementary.code')
os.system('cp -r ../application/Code.app ' + '/Applications/Code.app')

subprocess.call(['glib-compile-schemas', schemadir])
subprocess.call('gtk-update-icon-cache')
