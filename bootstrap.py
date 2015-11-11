#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, re
from docutils import nodes, utils
from docutils.parsers.rst.directives import images
from docutils.transforms import TransformError, Transform, parts
from docutils.parsers.rst import Directive, directives, states, roles
from docutils.writers.html4css1 import HTMLTranslator
from docutils.parsers.rst.roles import set_classes


# --- sidebar ---
def visit_sidebar(self, node):
    self.body.append(self.starttag(node, 'div', CLASS='offset1 span2 sidebar'))
    self.set_first_last(node)
    self.in_sidebar = True
def depart_sidebar(self, node):
    self.body.append('</div>\n')
    # HACK: add a trailing sidebar span for main content
    self.body.append('<div class="offset1 span7">\n')
    self.in_sidebar = False
HTMLTranslator.visit_sidebar = visit_sidebar
HTMLTranslator.depart_sidebar = depart_sidebar


# --- footer ---
def depart_footer(self, node):
    start = self.context.pop()
    footer = [self.starttag(node, 'div', CLASS='footer'),
              '<hr class="footer" />\n']
    footer.extend(self.body[start:])
    footer.append('\n</div>\n')
    # HACK: close the trailing sidebar span
    footer = [u'</div>\n</div>\n'] + footer
    self.footer.extend(footer)
    self.body_suffix[:0] = footer
    del self.body[start:]
HTMLTranslator.depart_footer = depart_footer


# --- html document ---
def html_depart_document(self, node):
    self.head_prefix.extend([self.doctype,
                             self.head_prefix_template %
                             {'lang': self.settings.language_code}])
    self.html_prolog.append(self.doctype)
    self.meta.insert(0, self.content_type % self.settings.output_encoding)
    self.head.insert(0, self.content_type % self.settings.output_encoding)
    if self.math_header:
        self.head.append(self.math_header)
    # skip content-type meta tag with interpolated charset value:
    self.html_head.extend(self.head[1:])
    # self.body_prefix.append(self.starttag(node, 'div', CLASS='document'))
    self.body_prefix.append(self.starttag(node, 'div', CLASS='container-fluid'))
    # self.body_suffix.insert(0, '</div>\n')
    self.fragment.extend(self.body) # self.fragment is the "naked" body
    self.html_body.extend(self.body_prefix[1:] + self.body_pre_docinfo
                          + self.docinfo + self.body
                          + self.body_suffix[:-1])
    assert not self.context, 'len(context) = %s' % len(self.context)
HTMLTranslator.depart_document = html_depart_document

# --- html container ---
def html_visit_container(self, node):
    self.body.append(self.starttag(node, 'div', CLASS=''))
HTMLTranslator.visit_container = html_visit_container

# ------------------------
# Remove compact paragraph
def visit_paragraph(self, node):
    #if self.should_be_compact_paragraph(node):
    #    self.context.append('')
    #else:
    self.body.append(self.starttag(node, 'p', ''))
    self.context.append('</p>\n')
HTMLTranslator.visit_paragraph = visit_paragraph


# -----------------------------------------------------------------------------
from docutils.core import publish_cmdline, default_description
description = ('Generates (X)HTML documents from standalone reStructuredText '
               'sources.  ' + default_description)
publish_cmdline(writer_name='html', description=description)

