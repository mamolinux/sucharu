#!/usr/bin/env python3

import os

VARIATIONS = ["Sucharu",
              "Sucharu-Darker",
              "Sucharu-Dark"]

DEST = '../../usr/share/themes'

curdir = os.getcwd()

print("Updating Gtk4 assets")
os.chdir("gtk-4.0/")
os.system("sassc ./sass/gtk.scss gtk.css")
os.system("sassc ./sass/gtk-dark.scss gtk-dark.css")
os.system("sassc ./sass/gtk-darker.scss gtk-darker.css")
os.system("./render-assets.sh")
print("Gtk4 assets updated")

os.chdir(curdir)

print("Updating Gtk3 assets")
os.chdir("gtk-3.0/")
os.system("sassc ./sass/gtk.scss gtk.css")
os.system("sassc ./sass/gtk-dark.scss gtk-dark.css")
os.system("sassc ./sass/gtk-darker.scss gtk-darker.css")
os.system("./render-assets.sh")
print("Gtk3 assets updated")

os.chdir(curdir)

print("Updating Gtk2 assets")
os.chdir("gtk-2.0/")
os.system("./render-assets.sh")
os.system("./render-dark-assets.sh")
print("Gtk2 assets updated")

os.chdir(curdir)

print("Updating Cinnamon assets")
os.chdir("cinnamon/")
os.system("sassc ./sass/cinnamon.scss cinnamon.css")
os.system("sassc ./sass/cinnamon-dark.scss cinnamon-dark.css")
print("Cinnamon assets updated")

os.chdir(curdir)

print("Updating Xfwm4 assets")
os.chdir("xfwm4/")
os.system("./render-assets.sh")

os.chdir(curdir)

print("Updating Xfwm4 dark assets")
os.chdir("xfwm4-dark/")
os.system("./render-assets.sh")

os.chdir(curdir)

if __name__ == '__main__':
    print("Building themes")
    for variation in VARIATIONS:
        dest_folder = os.path.join(DEST, variation)
        os.system("mkdir -p %s" % dest_folder)
        if variation == "Sucharu":
            print("    Building Sucharu")
            os.system("cp index.theme %s/" % dest_folder)
            # Gtk2
            version_folder = os.path.join(dest_folder, "gtk-2.0")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R gtk-2.0/assets %s" % version_folder)
            os.system("cp gtk-2.0/*.rc %s" % version_folder)
            os.system("cp gtk-2.0/gtkrc %s" % version_folder)
            # Gtk3
            version_folder = os.path.join(dest_folder, "gtk-3.0")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R gtk-3.0/assets %s" % version_folder)
            os.system("cp gtk-3.0/gtk.css %s" % version_folder)
            os.system("cp gtk-3.0/thumbnail.png %s" % version_folder)
            # Gtk4
            version_folder = os.path.join(dest_folder, "gtk-4.0")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R gtk-4.0/assets %s" % version_folder)
            os.system("cp gtk-4.0/gtk.css %s" % version_folder)
            # os.system("cp gtk-3.0/thumbnail.png %s" % version_folder)
            # Metacity
            os.system("cp -R metacity-1 %s" % dest_folder)
            os.system("rm %s/*-dark*" % (os.path.join(dest_folder, "metacity-1")))
            os.chdir((os.path.join(dest_folder, "metacity-1")))
            os.system("ln -sf %s %s" % ("metacity-theme-1.xml", "metacity-theme-2.xml"))
            os.system("ln -sf %s %s" % ("metacity-theme-1.xml", "metacity-theme-3.xml"))
            os.chdir(curdir)
            # Cinnamon
            version_folder = os.path.join(dest_folder, "cinnamon")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R cinnamon/common-assets %s" % version_folder)
            os.system("cp -R cinnamon/light-assets %s" % version_folder)
            os.system("cp cinnamon/sucharu-thumbnail.png %s" % os.path.join(version_folder, "thumbnail.png"))
            os.system("cp cinnamon/cinnamon.css %s" % version_folder)
            # XFWM
            os.system("cp -R xfwm4 %s" % dest_folder)
            
        elif variation == "Sucharu-Darker":
            print("    Building Sucharu-Darker")
            os.system("cp index.theme-darker %s" % os.path.join(dest_folder, "index.theme"))
            # Gtk2
            version_folder = os.path.join(dest_folder, "gtk-2.0")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R gtk-2.0/assets %s" % version_folder)
            # os.system("cp -R gtk-2.0/menubar-toolbar %s" % version_folder)
            os.system("cp gtk-2.0/*.rc %s" % version_folder)
            os.system("cp gtk-2.0/gtkrc-darker %s" % os.path.join(version_folder, "gtkrc"))
            # Gtk3
            version_folder = os.path.join(dest_folder, "gtk-3.0")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R gtk-3.0/assets %s" % version_folder)
            os.system("cp gtk-3.0/gtk-darker.css %s" % os.path.join(version_folder, "gtk.css"))
            os.system("cp gtk-3.0/thumbnail.png %s" % version_folder)
            # Gtk4
            version_folder = os.path.join(dest_folder, "gtk-4.0")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R gtk-4.0/assets %s" % version_folder)
            os.system("cp gtk-4.0/gtk-darker.css %s" % os.path.join(version_folder, "gtk.css"))
            # os.system("cp gtk-4.0/thumbnail.png %s" % version_folder)
            # XFWM
            version_folder = os.path.join(dest_folder, "xfwm4")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R xfwm4/*.png %s" % version_folder)
            os.system("cp -R xfwm4/themerc %s" % version_folder)

        elif variation == "Sucharu-Dark":
            print("    Building Sucharu-Dark")
            os.system("cp index.theme-dark %s" % os.path.join(dest_folder, "index.theme"))
            # Gtk2
            version_folder = os.path.join(dest_folder, "gtk-2.0")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R gtk-2.0/assets-dark %s" % version_folder)
            os.system("rm -rf %s" % os.path.join(version_folder, "assets"))
            os.system("mv %s %s" % (os.path.join(version_folder, "assets-dark"), os.path.join(version_folder, "assets")))
            os.system("cp gtk-2.0/*.rc %s" % version_folder)
            os.system("cp gtk-2.0/gtkrc-dark %s" % os.path.join(version_folder, "gtkrc"))
            os.system("cp gtk-2.0/menubar-toolbar-dark.rc %s" % os.path.join(version_folder, "menubar-toolbar.rc"))
            # Gtk3
            version_folder = os.path.join(dest_folder, "gtk-3.0")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R gtk-3.0/assets %s" % version_folder)
            os.system("cp gtk-3.0/gtk-dark.css %s" % os.path.join(version_folder, "gtk.css"))
            os.system("cp gtk-3.0/thumbnail-dark.png %s" % os.path.join(version_folder, "thumbnail.png"))
            # Gtk4
            version_folder = os.path.join(dest_folder, "gtk-4.0")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R gtk-4.0/assets %s" % version_folder)
            os.system("cp gtk-4.0/gtk-dark.css %s" % os.path.join(version_folder, "gtk.css"))
            # os.system("cp gtk-3.0/thumbnail-dark.png %s" % os.path.join(version_folder, "thumbnail.png"))
            # Metacity
            os.system("cp -R metacity-1 %s" % dest_folder)
            os.system("mv %s %s" % (os.path.join(dest_folder, "metacity-1", "metacity-theme-1-dark.xml"), os.path.join(dest_folder, "metacity-1", "metacity-theme-1.xml")))
            os.chdir((os.path.join(dest_folder, "metacity-1")))
            os.system("ln -sf %s %s" % ("metacity-theme-1.xml", "metacity-theme-2.xml"))
            os.system("ln -sf %s %s" % ("metacity-theme-1.xml", "metacity-theme-3.xml"))
            os.chdir(curdir)
            os.system("mv %s %s" % (os.path.join(dest_folder, "metacity-1", "thumbnail-dark.png"), os.path.join(dest_folder, "metacity-1", "thumbnail.png")))
            # Cinnamon
            version_folder = os.path.join(dest_folder, "cinnamon")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R cinnamon/common-assets %s" % version_folder)
            os.system("cp -R cinnamon/dark-assets %s" % version_folder)
            os.system("cp cinnamon/sucharu-dark-thumbnail.png %s" % os.path.join(version_folder, "thumbnail.png"))
            os.system("cp cinnamon/cinnamon-dark.css %s" % os.path.join(version_folder, "cinnamon.css"))
            # XFWM
            version_folder = os.path.join(dest_folder, "xfwm4")
            os.system("mkdir -p %s" % version_folder)
            os.system("cp -R xfwm4-dark/*.png %s" % version_folder)
            os.system("cp -R xfwm4-dark/themerc %s" % version_folder)
