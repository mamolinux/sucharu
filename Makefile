all: clean buildthemes

buildthemes:
	@echo "Building the themes"
	./generate-themes.py

clean:
	rm -rf usr __pycache__
