# Code for MacOS

MacOS port of elementary's code editor

<img width="1057" alt="Screenshot 2022-04-10 at 03 42 46" src="https://user-images.githubusercontent.com/44585538/162597553-299e6680-e55c-438f-8a61-2f321e8769b0.png">


## Building, Testing, and Installation


1. Clone repository
```
git clone https://github.com/timothyschoen/elementary.code_macOS.git
```

2. Install dependencies using homebrew (for installing homebrew see: https://brew.sh/)

```
brew install libgit2-glib libhandy vte3 libpeas gtk+3 vala guile libgee glib meson ninja gtksourceview4 editorconfig gsettings-desktop-schemas gtkspell3 gnome-icon-theme
```

3. Build sources:

On x64:
```
meson build --prefix=/usr/local/
cd build
ninja
```

On Apple Silicon:

```
meson build --prefix=/opt/homebrew/
cd build
ninja
```

3. Install
```
sudo ninja install
```

Installation is necessary because it
 1. Installs Glib schemas to $HOMEBREW_PATH/share/glib-2.0/schemas
 2. Installs elementary-icon-theme and elementary-gtk-theme
 3. Sets elementary-icon-theme and elementary-gtk-theme as defaults in ~/.config/gtk-3.0/settings.ini. This script will change your default gtk theme, be warned!! Not many apps on mac use gtk so it's probably not a big deal for most.

It will install the application to /Applications/Code.app

This is mostly for playing around, it works okay-ish. It can't receive Apple's "open file" commands, so I wrapped it in Applescript so you can at least open a file with while it's not already opened.

Plugins work, but only one a a time and they can be quite buggy.

