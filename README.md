# Code for MacOS

MacOS port of elementary's code editor

<img width="1082" alt="Screenshot 2022-04-10 at 00 59 52" src="https://user-images.githubusercontent.com/44585538/162594355-31bf90bf-65bc-4b30-8778-e771fbbc10b4.png">


## Building, Testing, and Installation

Replace $HOMEBREW_DIR with your homebrew directory, it can be /usr/local/ (x64) or /opt/homebrew (ARM)

1. Install dependencies using homebrew

```brew install libgit2-glib libhandy vte3 libsoup libpeas gtk+3 vala guile libgee glib meson gtksourceview4 editorconfig gsettings-desktop-schemas gtkspell3 appstream-glib gcc```

2. Build sources:
```
    meson build --prefix=$HOMEBREW_DIR
    cd build
    ninja
```

3. Copy glib schemas (app won't launch otherwise!)
    1. From ‘schemas’ to $HOMEBREW_DIR/share/glib-2.0/schemas

4. Install elementary icon theme
    1. Copy /icons/elementary to $HOMEBREW_DIR/share/icons/
    2. Set theme in ~/.config/gtk-3.0/settings.ini -> see /icons folder for settings.ini example

5. Package application (with AppleScript to allow open action) (TODO)

I'll create a simpler installation workflow soon!

This is mostly for playing around, it works okay-ish. It can't receive Apple's "open file" commands, so that part is still broken.

