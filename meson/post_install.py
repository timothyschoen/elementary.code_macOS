#!/usr/bin/env python3

import os
import subprocess
import platform

if platform.processor() == "arm":
    homebrewdir = os.path.join('/', 'opt', 'homebrew')
else:
    homebrewdir = os.path.join('/', 'usr', 'local')

iconsdir = os.path.join(os.getenv("HOME"), '.icons');
themesdir = os.path.join(os.getenv("HOME"), '.themes');
pluginsdir = os.path.join(homebrewdir, 'lib', 'io.elementary.code', 'plugins');

os.makedirs(pluginsdir, exist_ok=True)
os.makedirs(iconsdir, exist_ok=True)
os.makedirs(themesdir, exist_ok=True)
os.makedirs(os.getenv("HOME") + '/.config/gtk-3.0/', exist_ok=True)
os.makedirs(os.getenv("HOME") + '/.config/gtk-3.0/', exist_ok=True)

os.system('cp -r ../icons/elementary ' + iconsdir + '/elementary')
os.system('cp -r ../themes/io.elementary.stylesheet.strawberry ' + themesdir + '/io.elementary.stylesheet.strawberry')
os.system('cp ../meson/settings.ini ' + '~/.config/gtk-3.0/settings.ini')

os.makedirs("/opt/homebrew/lib/io.elementary.code/plugins", exist_ok=True)
os.makedirs("/opt/homebrew/lib/io.elementary.code/plugins/unused", exist_ok=True)

plugins = [
            'terminal',
            'brackets-completion',
            'detect-indent',
            'highlight-word-selection',
            'markdown-actions',
            'preserve-indent',
            'strip-trailing-save',
            'vim-emulation',
            'word-completion',
            'outline',
]
#for plugin in plugins:
#    path = pluginsdir + '/' + plugin + '/lib' + plugin;
#    os.system('mv ' + path + '.dylib ' + path + '.so') # hack to make it find the plugins

for plugin in plugins:
    path = pluginsdir + '/' + plugin;
    os.system('mv ' + path + ' ' + pluginsdir + '/unused/' + plugin)

# Only one plugin at a time currently supported...
current_plugin = 'spell'

path = pluginsdir + '/' + current_plugin + '/lib' + current_plugin
os.system('mv ' + path + '.dylib ' + path + '.so') # hack to make it find the plugins


os.system('cp ../meson/settings.ini ~/.config/gtk-3.0/settings.ini')

os.system('rm -rf /Applications/Code.app')
os.system('cp ../build/src/io.elementary.code ../application/Code.app/Contents/MacOS/Code')
os.system('cp -r -f ../application/Code.app /Applications/Code.app')

subprocess.call('gtk3-update-icon-cache')
