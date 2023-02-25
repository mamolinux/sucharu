SHELL:=/bin/bash

all: buildplankthemes
	
buildplankthemes:
	@echo "Building plank themes"
	mkdir -p usr/share/plank/themes
	@wait
	cp -Rv plank-themes/* usr/share/plank/themes/

clean:
	rm -rf usr
