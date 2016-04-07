STYLE = style.css
FLAGS = --stylesheet=$(STYLE) --link-stylesheet \
     --language=en --no-generator --no-source-link --no-datestamp \
     --section-numbering --output-encoding=UTF-8 --input-encoding=UTF-8 \
     --traceback --cloak-email-addresses

RST = ./rst2html.py
RM = /bin/rm
SOURCES=$(wildcard *.rst)
TARGETS=$(patsubst %.rst,%.html, $(SOURCES))

all: $(TARGETS)


%.html: %.rst
	@echo "Generating $@"
	@$(RST) $(FLAGS) $< $@
	@pygmentize -O full,linenos=1,encoding=utf8,style=tango  -f html -l rest -o $<.html $<

clean:
	@$(RM) -f $(TARGETS)
