#!/usr/bin/env python3

import os
import subprocess
import platform
import shlex

# returns true if a file is an OSX alias, false otherwise
def isAlias(path, already_checked_os=False):
    if (not already_checked_os) and ('Darwin' != platform.system()):  # already_checked just saves a few microseconds ;-)
        return False
    checkpath = os.path.abspath(path)       # osascript needs absolute paths
    # Next several lines are AppleScript
    line_1='tell application "Finder"'
    line_2='set theItem to (POSIX file "'+checkpath+'") as alias'
    line_3='if the kind of theItem is "alias" then'
    line_4='   return true'
    line_5='else'
    line_6='   return false'
    line_7='end if'
    line_8='end tell'
    cmd = "osascript -e '"+line_1+"' -e '"+line_2+"' -e '"+line_3+"' -e '"+line_4+"' -e '"+line_5+"' -e '"+line_6+"' -e '"+line_7+"' -e '"+line_8+"'"
    args = shlex.split(cmd)      # shlex splits cmd up appropriately so we can call subprocess.Popen with shell=False (better security)
    p = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    retval = p.wait()
    if (0 == retval):
        line = p.stdout.readlines()[0]
        line2 = line.decode('UTF-8').replace('\n','')
        if ('true' == line2):
            return True
        else:
            return False
    else:
        print('resolve_osx_alias: Error: subprocess returned non-zero exit code '+str(retval))
    return None


# returns the full path of the file "pointed to" by the alias
def resolve_osx_alias(path, already_checked_os=False, convert=False):        # single file/path name
    if (not already_checked_os) and ('Darwin' != platform.system()):  # already_checked just saves a few microseconds ;-)
        return path
    checkpath = os.path.abspath(path)       # osascript needs absolute paths
    # Next several lines are AppleScript
    line_1='tell application "Finder"'
    line_2='set theItem to (POSIX file "'+checkpath+'") as alias'
    line_3='if the kind of theItem is "alias" then'
    line_4='   get the posix path of (original item of theItem as text)'
    line_5='else'
    line_6='return "'+checkpath+'"'
    line_7 ='end if'
    line_8 ='end tell'
    cmd = "osascript -e '"+line_1+"' -e '"+line_2+"' -e '"+line_3+"' -e '"+line_4+"' -e '"+line_5+"' -e '"+line_6+"' -e '"+line_7+"' -e '"+line_8+"'"
    args = shlex.split(cmd)              # shlex splits cmd up appropriately so we can call subprocess.Popen with shell=False (better security)
    p = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    retval = p.wait()
    if (0 == retval):
        line = p.stdout.readlines()[0]
        source = line.decode('UTF-8').replace('\n','')
        if (convert):
            os.remove(checkpath)
            os.symlink(source, checkpath)
    else:
        print('resolve_osx_aliases: Error: subprocess returned non-zero exit code '+str(retval))
        source = ''
    return source


if platform.processor() == "arm":
    homebrewdir = os.path.join('/', 'opt', 'homebrew')
else:
    homebrewdir = os.path.join('/', 'usr', 'local')


schemadir = os.path.join(homebrewdir, 'share', 'glib-2.0', 'schemas');
iconsdir = os.path.join(homebrewdir, 'share', 'icons');
themesdir = os.path.join(homebrewdir, 'share', 'themes');

if isAlias(themesdir):
    themesdir = resolve_osx_alias(themesdir, True)
if isAlias(iconsdir):
    iconsdir = resolve_osx_alias(iconsdir, True)

os.makedirs(os.getenv("HOME") + '/.config/gtk-3.0/', exist_ok=True)
os.makedirs(os.getenv("HOME") + '/.config/gtk-3.0/', exist_ok=True)

os.system('cp ../schema/* ' + schemadir)
os.system('cp -r ../icons/elementary ' + iconsdir + '/elementary')
os.system('cp -r ../themes/io.elementary.strawberry ' + themesdir + '/io.elementary.strawberry')
os.system('cp ../meson/settings.ini ' + '~/.config/gtk-3.0/settings.ini')

os.system('cp ../build/src/io.elementary.code ' + '../application/Code.app/Contents/MacOS/io.elementary.code')
os.system('cp -r ../application/Code.app ' + '/Applications/Code.app')

subprocess.call(['glib-compile-schemas', schemadir])
subprocess.call('gtk3-update-icon-cache')
