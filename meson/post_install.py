#!/usr/bin/env python3

import os
import subprocess
import platform

if platform.processor() == "arm":
    homebrewdir = os.path.join('/', 'opt', 'homebrew')
else:
    homebrewdir = os.path.join('/', 'usr', 'local')

schemadir = os.path.join(homebrewdir, 'share', 'glib-2.0', 'schemas');
iconsdir = os.path.join(os.getenv("HOME"), '.icons');
themesdir = os.path.join(os.getenv("HOME"), '.themes');
pluginsdir = os.path.join(homebrewdir, 'lib', 'io.elementary.code', 'plugins');

os.makedirs(pluginsdir, exist_ok=True)
os.makedirs(iconsdir, exist_ok=True)
os.makedirs(themesdir, exist_ok=True)
os.makedirs(os.getenv("HOME") + '/.config/gtk-3.0/', exist_ok=True)
os.makedirs(os.getenv("HOME") + '/.config/gtk-3.0/', exist_ok=True)

os.system('cp ../schema/* ' + schemadir)
os.system('cp -r ../icons/elementary ' + iconsdir + '/elementary')
os.system('cp -r ../themes/io.elementary.stylesheet.strawberry ' + themesdir + '/io.elementary.stylesheet.strawberry')
os.system('cp ../meson/settings.ini ' + '~/.config/gtk-3.0/settings.ini')


#plugins = [
#            'terminal',
#            'spell',
#            'brackets-completion',
#            'detect-indent',
#            'highlight-word-selection',
#            'markdown-actions',
#            'preserve-indent',
#            'strip-trailing-save',
#            'vim-emulation',
#            'word-completion'
#]
#for plugin in plugins:
#    path = pluginsdir + '/' + plugin + '/lib' + plugin;
#    os.system('mv ' + path + '.dylib ' + path + '.so') # hack to make it find the plugins

# Only one plugin at a time currently supported...
current_plugin = 'spell'

path = pluginsdir + '/' + current_plugin + '/lib' + current_plugin;
os.system('mv ' + path + '.dylib ' + path + '.so') # hack to make it find the plugins


os.system('cp ../meson/settings.ini ' + '~/.config/gtk-3.0/settings.ini')

os.system('cp ../build/src/io.elementary.code ' + '../application/Code.app/Contents/MacOS/io.elementary.code')
os.system('cp -r ../application/Code.app ' + '/Applications/Code.app')

os.makedirs("/opt/homebrew/lib/io.elementary.code/plugins", exist_ok=True)

subprocess.call(['glib-compile-schemas', schemadir])
subprocess.call('gtk3-update-icon-cache')
