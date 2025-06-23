#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# rename and install gtk thumbnails for cinnamon

import os
import sys

PREFIX = os.environ.get('MESON_INSTALL_DESTDIR_PREFIX', '/usr')
svg_src = sys.argv[1]
png_dir = os.path.join(PREFIX, sys.argv[2])
svg_dir = os.path.dirname(svg_src)
png_thumb = os.path.join(svg_dir, 'thumbnail.png')

if __name__ == '__main__':
	os.makedirs(png_dir, exist_ok=True)
	os.system('inkscape %s -o %s --export-dpi=192' % (svg_src, png_thumb))
	os.system('optipng -o7 %s' % png_thumb)
	os.system('cp -uv %s %s' % (png_thumb, os.path.join(png_dir, 'thumbnail.png')))
