#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, re
from docutils import nodes, utils
from docutils.parsers.rst.directives import images
from docutils.transforms import TransformError, Transform, parts
from docutils.parsers.rst import Directive, directives, states, roles
from docutils.writers.html4css1 import HTMLTranslator
from docutils.parsers.rst.roles import set_classes


def visit_bullet_list(self, node):
    atts = {}
    old_compact_simple = self.compact_simple
    self.context.append((self.compact_simple, self.compact_p))
    self.compact_p = None
    self.compact_simple = self.is_compactable(node)
    if self.compact_simple and not old_compact_simple:
        atts['class'] = 'thumbnail'
    self.body.append(self.starttag(node, 'ul', **atts))
def depart_bullet_list(self, node):
    self.compact_simple, self.compact_p = self.context.pop()
    self.body.append('</ul>\n')
HTMLTranslator.visit_bullet_list = visit_bullet_list
HTMLTranslator.depart_bullet_list = depart_bullet_list


def visit_list_item(self, node):
    self.body.append(self.starttag(node, 'li', CLASS='span2'))
    node[0]['classes'].append('thumbnail')
def depart_list_item(self, node):
    self.body.append('</li>\n')
HTMLTranslator.visit_list_item = visit_list_item
HTMLTranslator.depart_list_item = depart_list_item


# -----------------------------------------------------------------------------
from docutils.core import publish_cmdline, default_description
description = ('Generates (X)HTML documents from standalone reStructuredText '
               'sources.  ' + default_description)
publish_cmdline(writer_name='html', description=description)

