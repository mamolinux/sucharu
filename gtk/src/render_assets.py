#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import subprocess
import argparse

from pathlib import Path
from multiprocessing import cpu_count, Pool

# Default values
DEFAULT_FORCE = False
DEFAULT_OPTIMIZE = True
DEFAULT_SVG='assets.svg'
INKSCAPE = "/usr/bin/inkscape"
OPTIPNG = "/usr/bin/optipng"

def run_command(cmd, cwd=None):
	print(f"> {cmd}")
	subprocess.run(cmd, shell=True, check=True, cwd=cwd)

def render(args_tuple):
	id, asset, cwd, src, optimize, dpi = args_tuple
	print(f"\nRendering {asset}.png")
	cmd = f"{INKSCAPE} --export-id={id} --export-id-only --export-dpi={dpi} -o {asset}.png {src} > /dev/null"
	run_command(cmd, cwd)
	if optimize:
		# print(f"\Optimizing {asset}.png")
		cmd = f"{OPTIPNG} -o7 --quiet {asset}.png"
		run_command(cmd, cwd)

def render_asets(args):
	if (not args.dir) and (not args.svg):
		sys.exit()
	ASSETS_DIR = "assets"
	if ((not args.dir) and args.svg):
		svg_dir = os.path.dirname(args.svg)
		SRC_FILE = args.svg
	else:
		svg_dir = args.dir
		SRC_FILE = f"{svg_dir}/{args.svg}"
	
	num_cores = cpu_count()
	p = Pool(processes=num_cores)
	Path(os.path.join(svg_dir, ASSETS_DIR)).mkdir(parents=True, exist_ok=True)
	
	if ("gtk-3.0" in svg_dir) or ("gtk-4.0" in svg_dir):
		index = open(f"{svg_dir}/assets.txt", 'r').read().splitlines()
		args_tuple_list = []
		for i in index:
			if (args.asset and (args.asset not in i)):
				continue
			asset = os.path.join(svg_dir, ASSETS_DIR, f"{i}")
			if os.path.exists(f"{asset}.png") and (not args.force):
				print(f"{asset}.png exists.")
			else:
				args_tuple_list.append((i, asset, svg_dir, SRC_FILE, args.optimize, 96))
		
			asset2 = os.path.join(svg_dir, ASSETS_DIR, f"{i.strip()}@2")
			if os.path.exists(f"{asset2}.png") and (not args.force):
				print(f"{asset2}.png exists.")
			else:
				args_tuple_list.append((i, asset2, svg_dir, SRC_FILE, args.optimize, 192))
		with p:
			p.map(render, args_tuple_list)

def parse_args():
	parser = argparse.ArgumentParser(
		description="Render script for gtk assets."
	)
	parser.add_argument("-d", "--dir", type=str, help="Folder containing the svg asset.")
	parser.add_argument("-a", "--asset", type=str, default="", help="render only the asset matching the name")
	parser.add_argument("-f", "--force", action="store_true", default=DEFAULT_FORCE, help="Force rendering of existing generated assets (default: False)")
	parser.add_argument("-o", "--optimize", action="store_true", default=DEFAULT_OPTIMIZE, help="Optimize PNG files (default: True)")
	parser.add_argument("-s", "--svg", type=str, default=DEFAULT_SVG, help="SVG file name (default: assets.svg)")
	args = parser.parse_args()

	return args

if __name__ == '__main__':
	render_asets(parse_args())
