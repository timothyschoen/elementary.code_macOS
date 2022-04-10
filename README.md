# Code for MacOS

MacOS port of elementary's code editor

<img width="1082" alt="Screenshot 2022-04-10 at 00 59 52" src="https://user-images.githubusercontent.com/44585538/162594355-31bf90bf-65bc-4b30-8778-e771fbbc10b4.png">


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

Installation is necessary because it moves some glib schemas that the app needs in order to launch.

It also copies the elementary-icon-theme to $HOMEBREW_DIR/share/icons/ and sets it as the default theme in ~/.config/gtk-3.0/settings.ini
So this script will change your default gtk theme, be warned!! Not many apps on mac use gtk so it's probably not a big deal for most.

It will install the application to /Applications/Code.app

This is mostly for playing around, it works okay-ish. It can't receive Apple's "open file" commands, so that part is still broken.

