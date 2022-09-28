# [Sucharu Themes](https://hsbasu.github.io/sucharu)

<p align="center">
	<a href="https://github.com/hsbasu/sucharu/blob/master/LICENSE">
		<img src="https://img.shields.io/github/license/hsbasu/sucharu?label=License" alt="License"
	</a>
  	<a href="#">
		<img src="https://img.shields.io/github/repo-size/hsbasu/sucharu?label=Repo%20size" alt="GitHub repo size">
  	</a>
	<a href="https://github.com/hsbasu/sucharu/issues" target="_blank">
		<img src="https://img.shields.io/github/issues/hsbasu/sucharu?label=Issues" alt="Open Issues">
	</a>
	<a href="https://github.com/hsbasu/sucharu/pulls" target="_blank">
		<img src="https://img.shields.io/github/issues-pr/hsbasu/sucharu?label=PR" alt="Open PRs">
	</a>
  	<a href="https://github.com/hsbasu/sucharu/releases/latest">
		<img src="https://img.shields.io/github/v/release/hsbasu/sucharu?label=Latest%20Stable%20Release" alt="GitHub release (latest by date)">
  	</a>
	<a href="#download-latest-version">
		<img src="https://img.shields.io/github/downloads/hsbasu/sucharu/total?label=Downloads" alt="Downloads">
	</a>
	<a href="https://github.com/hsbasu/sucharu/releases/download/2.0.5/sucharu-theme-cinnamon-shell_2.0.5_all.deb">
		<img src="https://img.shields.io/github/downloads/hsbasu/sucharu/2.0.5/sucharu-theme-cinnamon-shell_2.0.5_all.deb?color=blue&label=Downloads%40Latest%20Binary" alt="GitHub release (latest by date and asset)">
	</a>
	<a href="https://github.com/hsbasu/sucharu/releases/download/2.0.5/sucharu-theme-gnome-shell_2.0.5_all.deb">
		<img src="https://img.shields.io/github/downloads/hsbasu/sucharu/2.0.5/sucharu-theme-gnome-shell_2.0.5_all.deb?color=blue&label=Downloads%40Latest%20Binary" alt="GitHub release (latest by date and asset)">
	</a>
	<a href="https://github.com/hsbasu/sucharu/releases/download/2.0.5/sucharu-theme-gtk_2.0.5_all.deb">
		<img src="https://img.shields.io/github/downloads/hsbasu/sucharu/2.0.5/sucharu-theme-gtk_2.0.5_all.deb?color=blue&label=Downloads%40Latest%20Binary" alt="GitHub release (latest by date and asset)">
	</a>
	<a href="https://github.com/hsbasu/sucharu/releases/download/2.0.5/sucharu-theme-plank_2.0.5_all.deb">
		<img src="https://img.shields.io/github/downloads/hsbasu/sucharu/2.0.5/sucharu-theme-plank_2.0.5_all.deb?color=blue&label=Downloads%40Latest%20Binary" alt="GitHub release (latest by date and asset)">
	</a>
	<a href="https://github.com/hsbasu/sucharu/releases/download/2.0.5/sucharu-themes_2.0.5_all.deb">
		<img src="https://img.shields.io/github/downloads/hsbasu/sucharu/2.0.5/sucharu-themes_2.0.5_all.deb?color=blue&label=Downloads%40Latest%20Binary" alt="GitHub release (latest by date and asset)">
	</a>
</p>

A theme package with mac-styled 3D title buttons and circular components.

## Download Latest Version
<p align="center">
	<a href="https://github.com/hsbasu/sucharu/zipball/master">Download Source (.zip)</a></br>
	<a href="https://github.com/hsbasu/sucharu/tarball/master">Download Source (.tar.gz)</a></br>
	<a href="https://github.com/hsbasu/sucharu/releases/download/2.0.5/sucharu-theme-cinnamon-shell_2.0.5_all.deb">Download Cinnamon Shell Binary (.deb)</a></br>
	<a href="https://github.com/hsbasu/sucharu/releases/download/2.0.5/sucharu-theme-gnome-shell_2.0.5_all.deb">Download GNOME Shell Binary (.deb)</a></br>
	<a href="https://github.com/hsbasu/sucharu/releases/download/2.0.5/sucharu-theme-gtk_2.0.5_all.deb">Download GNOME Shell Binary (.deb)</a></br>
	<a href="https://github.com/hsbasu/sucharu/releases/download/2.0.5/sucharu-theme-plank_2.0.5_all.deb">Download Plank Binary (.deb)</a></br>
	<a href="https://github.com/hsbasu/sucharu/releases/download/2.0.5/sucharu-themes_2.0.5_all.deb">Download GTK, Metacity and XFWM Binary (.deb)</a>
</p>

## Features and Screenshots

This package provides theme for components:
1. Gnome-shell
2. Cinnmon-shell
3. Gtk-2.0
4. Gtk-3.0
5. Gtk-4.0
6. Metacity
7. Xfwm
8. Plank

This theme is based on [Yaru](https://github.com/ubuntu/yaru) and [Mint-Y](https://github.com/linuxmint/mint-themes) themes.

<p align="center">
	<img src="#" alt="Main Window (Light)">
	<img src="#" alt="Main Window (Dark)">
</p>


## Contents
- [Download Latest Version](#download-latest-version)
- [Features and Screenshots](#features-and-screenshots)
- [Dependencies](#dependencies)
	- [Debian/Ubuntu based systems](#debianubuntu-based-distro)
	- [Other Linux-based systems](#other-linux-based-distro)
- [Installation](#build-and-install-the-latest-version)
	- [Debian/Ubuntu based systems](#debianubuntu-based-systems)
	- [Other Linux-based systems](#other-linux-based-systems)
	- [For Developers](#for-developers)
- [User Manual](#user-manual)
- [Issue Tracking and Contributing](#issue-tracking-and-contributing)
- [Contributors](#contributors)
	- [Authors](#author)

## Dependencies
```
debhelper ( >= 13 )
gnome-themes-standard
gtk2-engines-murrine
gtk2-engines-pixbuf
inkscape
python3
sassc
meson ( >= 0.60 )
```
### Debian/Ubuntu based distro
To install the build dependencies on Debian/Ubuntu based systems, run:
```
sudo apt install debhelper gnome-themes-standard gtk2-engines-murrine \
gtk2-engines-pixbuf inkscape python3 sassc meson
```

### Other Linux-based distro
Remove `apt install` and the `debhelper` package in the command given in [Debian/Ubuntu based distros](#debianubuntu-based-distro) and use the command for the package manager of the target system(eg. `yum install`, `dnf install`, `pacman -S` etc.)

**Note**: There might be cases where one or more dependencies might not be available for your system. But that is highly unlikely. In such situations, please [create an issue](#issue-tracking-and-contributing).

## Build and Install the Latest Version
### Debian/Ubuntu based systems
There are two methods, these themes can be installed/used on a Debian/Ubuntu based system. First, download and unzip the source package using:
```
wget https://github.com/hsbasu/sucharu/archive/refs/heads/master.zip
unzip master.zip
cd sucharu-master
```

1. **Option 1:** Manually copying necessary files to root (`/`). For that, follow the steps below:
	1. To build the themes, run:
		```
		make clean
		make all
		```
		from the `/path/to/repo` in a terminal. It will create the **GTK**, **Metacity**, **XFWM** and **Cinnamon** themes in `usr/share/themes`, and **Plank themes** in `usr/share/plank/themes`.

	2. Copy the contents of `usr/` to `/usr/`:
		```
		sudo cp -R usr /
		```
	3. To build **gnome-shell**, use meson as,
		```
		meson builddir
		meson compile -C builddir
		meson install -C builddir
		```

2. **Option 2:** Build debian packages and install it. To build a debian package on your own:
	1. from the `/path/to/repo` run:
		```
		dpkg-buildpackage --no-sign
		```
		This will create `sucharu-theme*.deb` packages at `../path/to/repo`.
	2. Install the debian packages using
		```
		sudo dpkg -i *.deb
		sudo apt install -f
		```
	After it is installed, set the themes from your distro's theme manager or use the [**Theme Manager**](https://hsbasu.github.io/theme-manager) to change themes automatically after certain periods.

### Other Linux-based systems
1. Install the [dependencies](#other-linux-based-distro).
2. From instructions for [Debian/Ubuntu based systems](#debianubuntu-based-systems), follow **Option 1**.

### For Developers
Coming Soon or create a PR.

## User Manual
Coming Soon or create a PR.

## Issue Tracking and Contributing
If you are interested to contribute and enrich the code, you are most welcome. You can do it by:
1. If you find a bug, to open a new issue with details: [Click Here](https://github.com/hsbasu/sucharu/issues)
2. If you know how to fix a bug or want to add new feature/documentation to the existing package, please create a [Pull Request](https://github.com/hsbasu/sucharu/compare).

## Contributors

### Author
[Himadri Sekhar Basu](https://github.com/hsbasu) is the author and current maintainer.

## Donations
I am a freelance programmer. So, If you like these themes and would like to offer me a coffee ( &#9749; ) to motivate me further, you can do so via:

[![](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/hsbasu/donate)
[![](https://www.paypalobjects.com/webstatic/i/logo/rebrand/ppcom.svg)](https://paypal.me/hsbasu)
[![](https://hsbasu.github.io/styles/icons/logo/svg/upi-logo.svg)](https://hsbasu.github.io/images/upi-qr.jpg)
