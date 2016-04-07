MAKE             = /usr/bin/make
RST2HTML         = ./thumbnails.py
RST2HTML_OPTIONS = --strip-comments \
				   --template=thumbnails.tmpl

SOURCES = scientific.txt    \
	      neurosciences.txt \
		  gnu-tux-1.txt     \
		  gnu-tux-2.txt     \
		  gnu-tux-3.txt     \
		  go.txt            \
		  misc-1.txt        \
		  misc-2.txt        \
		  nudes.txt 

OBJECTS = $(subst .txt,.html, $(SOURCES))

PNG_IMAGES = $(wildcard images/*.png)
PNG_THUMBNAILS = $(patsubst images%.png,thumbnails%.png, $(PNG_IMAGES))

JPG_IMAGES = $(wildcard images/*.jpg)
JPG_THUMBNAILS = $(patsubst images%.jpg,thumbnails%.jpg, $(JPG_IMAGES))

PHOTOS = $(wildcard photos/*.jpg)
THUMBNAILS = $(patsubst photos%.jpg,photos/thumbnails%.jpg, $(PHOTOS))

all: $(THUMBNAILS) $(PNG_THUMBNAILS) $(JPG_THUMBNAILS) $(OBJECTS)

thumbnails/%.png: images/%.png
	@echo "Making $< thumbnail"
	@convert -geometry x256 $< $@

thumbnails/%.jpg: images/%.jpg
	@echo "Making $< thumbnail"
	@convert -geometry x256 $< $@

photos/thumbnails/%.jpg: photos/%.jpg
	@echo "Making $< thumbnail"
	@convert -geometry x256 $< $@

%.html: %.txt 
	@echo "  - $@"
	@$(RST2HTML) $(RST2HTML_OPTIONS) $< $@

clean:
	@-rm -f $(OBJECTS)

distclean: clean
	@-rm -f `find . -name "*~"`

.PHONY: all clean distclean

