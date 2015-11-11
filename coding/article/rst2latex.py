#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes, utils
from docutils.parsers.rst import Directive, directives, states, roles
from docutils.parsers.rst.directives.images import Figure as OldFigure
from docutils.parsers.rst.directives.images import Image
from docutils.parsers.rst.roles import set_classes
from docutils.nodes import fully_normalize_name, whitespace_normalize_name
from docutils.transforms import TransformError, Transform, parts
from docutils.writers.latex2e import LaTeXTranslator
import sys, os, re


class math(nodes.Inline, nodes.TextElement):     pass
class nosectnum(nodes.Inline,nodes.TextElement): pass
class displaymath(nodes.Part, nodes.Element):    pass
class eqref(nodes.Inline, nodes.TextElement):    pass
class figref(nodes.Inline, nodes.TextElement):   pass
class abstract(nodes.General, nodes.Element):    pass
class keywords(nodes.General, nodes.Element):    pass
class video(nodes.General, nodes.Inline, nodes.Element): pass
class media(nodes.General, nodes.Inline, nodes.Element): pass


# --- bib_reference -----------------------------------------------------------
#
# 
#
def bib_reference(text):
    if not ':' in text:
        return text
    authors,date = text.split(':')
    authors = authors.split('+')
    if authors[-1] == 'Al':
        return authors[0] + ' et al. ' + date
    elif len(authors) == 1:
        return authors[0] + ' ' + date
    elif len(authors) == 2:
        return authors[0] + ' and ' + authors[1] + ' ' + date
    else:
        return authors[0] + ' et al. ' + date

# --- bib_entry ---------------------------------------------------------------
#
# 
#
def bib_entry(text):
    if not ':' in text:
        return text
    authors,date = text.split(':')
    authors = authors.split('+')
    if authors[-1] == 'Al':
        return authors[0] + ' et al. (' + date + ')'
    elif len(authors) == 1:
        return authors[0] + ' (' + date + ')'
    elif len(authors) == 2:
        return authors[0] + ' and ' + authors[1] + ' (' + date + ')'
    else:
        return authors[0] + ' et al. (' + date + ')'


# --- wrap display math -------------------------------------------------------
#
# 
#
def wrap_displaymath(math, label):
    parts = math.split('\n\n')
    ret = []
    for i, part in enumerate(parts):
        if label is not None and i == 0:
            ret.append('\\begin{split}%s\\end{split}' % part +
                       (label and '\\label{'+label+'}' or ''))
        else:
            ret.append('\\begin{split}%s\\end{split}\\notag' % part)
    return '\\begin{gather}\n' + '\\\\'.join(ret) + '\n\\end{gather}'


# --- sectnum transform -------------------------------------------------------
#
#  This sectnum tranform takes care of nosectnum directives
#
class SectNum(parts.SectNum):
    def update_section_numbers(self, node, prefix=(), depth=0):
        depth += 1
        if prefix:
            sectnum = 1
        else:
            sectnum = self.startvalue
        for child in node:
            if isinstance(child, nodes.section):
                numbers = prefix + (str(sectnum),)
                title = child[0]
                if not child.traverse(nosectnum):
                    # Use &nbsp; for spacing:
                    generated = nodes.generated(
                        '', (self.prefix + '.'.join(numbers) + self.suffix
                             +  u'\u00a0' * 3),
                        classes=['sectnum'])
                    title.insert(0, generated)
                    title['auto'] = 1
                if depth < self.maxdepth:
                    self.update_section_numbers(child, numbers, depth)
                sectnum += 1


# --- Equation references -----------------------------------------------------
#
# This class solves pending equation references throughout the whole document
#
class EquationReferences(Transform):
    default_priority = 260
    def apply(self):
        num = 0
        numbers = {}
        for node in self.document.traverse(displaymath):
            if node['label'] is not None:
                num += 1
                node['number'] = num
                numbers[node['label']] = num
            else:
                node['number'] = None
        for node in self.document.traverse(eqref):
            if node['target'] not in numbers:
                continue
            num = '(%d)' % numbers[node['target']]
            node[0] = nodes.Text(num, num)


# --- Figure references -------------------------------------------------------
#
# This class solves pending figure references throughout the whole document
#
class FigureReferences(Transform):
    default_priority = 260
    def apply(self):
        num = 0
        numbers = {}
        for node in self.document.traverse(nodes.figure):
            if node['label'] is not None:
                num += 1
                node['number'] = num
                numbers[node['label']] = num
            else:
                node['number'] = None
        for node in self.document.traverse(figref):
            if node['target'] not in numbers:
                continue
            num = '(%d)' % numbers[node['target']]
            node[0] = nodes.Text(num, num)


# --- math directive ----------------------------------------------------------
#
#
#
class Math(Directive):
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = { 'label': directives.unchanged,
                    'nowrap': directives.flag}
    def run(self):
        latex = '\n'.join(self.content)
        if self.arguments and self.arguments[0]:
            latex = self.arguments[0] + '\n\n' + latex
        node = displaymath()
        node['latex'] = latex
        node['label'] = self.options.get('label', None)
        node['nowrap'] = 'nowrap' in self.options
        ret = [node]
        if node['label']:
            tnode = nodes.target('', '', ids=['equation-' + node['label']])
            self.state.document.note_explicit_target(tnode)
            ret.insert(0, tnode)
        return ret
directives.register_directive('math', Math)


# --- abstract directive ------------------------------------------------------
#
#  
#
class Abstract(Directive):
    required_arguments, optional_arguments = 0,1
    final_argument_whitespace = True
    has_content = True
    def run(self):
        self.assert_has_content()
        node = abstract(self.block_text, **self.options)
        if self.arguments:
            node['title'] = self.arguments[0]
        else:
            node['title'] = u'Abstract'
        node['abstract'] = u'\n'.join(self.content)
        return [node]
directives.register_directive('abstract', Abstract)


# --- keywords directive ------------------------------------------------------
#
# 
#
class Keywords(Directive):
    required_arguments, optional_arguments = 0,1
    final_argument_whitespace = True
    has_content = True
    def run(self):
        self.assert_has_content()
        node = keywords(self.block_text, **self.options)
        if self.arguments:
            node['title'] = self.arguments[0]
        else:
            node['title'] = u'Keywords'
        node['keywords'] = u'\n'.join(self.content)
        return [node]
directives.register_directive('keywords', Keywords)


# --- video directive ---------------------------------------------------------
#
# Video inclusion
#
class Video(Image):
    """ Video inclusion """
    def align(argument):
        return directives.choice(argument, Image.align_h_values)
    option_spec = {'autoplay': directives.flag,
                   'loop': directives.flag,
                   'controls': directives.flag,
                   'height': directives.length_or_unitless,
                   'width': directives.length_or_percentage_or_unitless,
                   'align': align,
                   'class': directives.class_option}
    def run(self):
        old_image_node = nodes.image
        nodes.image = video
        node = Image.run(self)
        nodes.image = old_image_node
        return node
directives.register_directive('video', Video)

# --- media directive ---------------------------------------------------------
#
# Video or image (based on uri extension)
#
class Media(Video,Image):
    ''' Media inclusion '''
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec  = Image.option_spec.copy()
    option_spec.update(Video.option_spec.copy())
    def run(self):
        uri = directives.uri(self.arguments[0])
        if uri.split('.')[-1] in ['ogg', 'mpg', 'mp4', 'avi', 'mpeg']:
            return Video.run(self)
        else:
            return Image.run(self)
directives.register_directive('media', Media)

# --- figure directive --------------------------------------------------------
#
# figure redefinition to include image or movie inside
#
class Figure(Media):
    """ Figure with caption """
    def align(argument):
        return directives.choice(argument, Image.align_h_values)
    def figwidth_value(argument):
        if argument.lower() == 'image':
            return 'image'
        else:
            return directives.length_or_percentage_or_unitless(argument, 'px')
    option_spec = Media.option_spec.copy()
    option_spec['label'] = directives.unchanged_required
    option_spec['figwidth'] = figwidth_value
    option_spec['figclass'] = directives.class_option
    option_spec['align'] = align
    has_content = True
    def run(self):
        figwidth = self.options.pop('figwidth', None)
        figclasses = self.options.pop('figclass', None)
        align = self.options.pop('align', None)
        (media_node,) = Media.run(self)
        if isinstance(media_node, nodes.system_message):
            return [media_node]
        figure_node = nodes.figure('', media_node)
        if figwidth == 'image':
            if PIL and self.state.document.settings.file_insertion_enabled:
                # PIL doesn't like Unicode paths:
                try:
                    i = PIL.open(str(media_node['uri']))
                except (IOError, UnicodeError):
                    pass
                else:
                    self.state.document.settings.record_dependencies.add(
                        media_node['uri'])
                    figure_node['width'] = i.size[0]
        elif figwidth is not None:
            figure_node['width'] = figwidth
        if figclasses:
            figure_node['classes'] += figclasses
        if align:
            figure_node['align'] = align
        if self.content:
            node = nodes.Element()          # anonymous container for parsing
            self.state.nested_parse(self.content, self.content_offset, node)
            first_node = node[0]
            if isinstance(first_node, nodes.paragraph):
                caption = nodes.caption(first_node.rawsource, '',
                                        *first_node.children)
                figure_node += caption
            elif not (isinstance(first_node, nodes.comment)
                      and len(first_node) == 0):
                error = self.state_machine.reporter.error(
                      'Figure caption must be a paragraph or empty comment.',
                      nodes.literal_block(self.block_text, self.block_text),
                      line=self.lineno)
                return [figure_node, error]
            if len(node) > 1:
                figure_node += nodes.legend('', *node[1:])
        node = figure_node

        node['label'] = self.options.get('label', None)
        if not node['label']:
            node['label'] = self.options.get('uri')
        node['number'] = None
        ret = [node]
        if node['label']:
            key = node['label']
            tnode = nodes.target('', '', ids=['figure-' + node['label']])
            self.state.document.note_explicit_target(tnode)
            ret.insert(0, tnode)
        return ret
directives.register_directive('figure', Figure)


# --- sectnum directive --------------------------------------------------------
#
# 
#
class Sectnum(Directive):
    """Automatic section numbering."""

    option_spec = {'depth': int,
                   'start': int,
                   'prefix': directives.unchanged_required,
                   'suffix': directives.unchanged_required}
    def run(self):
        pending = nodes.pending(SectNum)
        pending.details.update(self.options)
        self.state_machine.document.note_pending(pending)
        return [pending]
directives.register_directive('sectnum', Sectnum)

# --- nosectnum directive -----------------------------------------------------
#
# 
#
class NoSectnum(Directive):
    """Disable automatic section numbering."""
    required_arguments, optional_arguments = 0,0
    final_argument_whitespace = True
    has_content = False
    def run(self):
        node = nosectnum(self.block_text, **self.options)
        return [node]
directives.register_directive('nosectnum', NoSectnum)


# --- math role ---------------------------------------------------------------
#
# 
#
def math_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    latex = utils.unescape(text, restore_backslashes=True)
    return [math(latex=latex)], []
math_role.content = True
roles.register_canonical_role('math', math_role)




# --- eq role -----------------------------------------------------------------
# 
# `eq` role allows to refer to an equation identified by a label
#
def eq_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    text = utils.unescape(text)
    node = eqref('(?)', '(?)', target=text)
    pending = nodes.pending(EquationReferences)
    inliner.document.note_pending(pending)
    return [node], []
eq_role.content = True
roles.register_canonical_role('eq', eq_role)


# --- fig role ----------------------------------------------------------------
#
# `fig` role allows to refer to a figure identified by a label
#
def fig_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    text = utils.unescape(text)
    node = figref('(?)', '(?)', target=text)
    pending = nodes.pending(FigureReferences)
    inliner.document.note_pending(pending)
    return [node], []
fig_role.content = True
roles.register_canonical_role('fig', fig_role)



# --- latex eqref --------------------------------------------------------------
def latex_visit_eqref(self, node):
    raise nodes.SkipNode
def latex_depart_eqref(self, node):
    raise nodes.SkipNode
LaTeXTranslator.visit_eqref = latex_visit_eqref
LaTeXTranslator.depart_eqref = latex_depart_eqref

# --- latex figref --------------------------------------------------------------
def latex_visit_figref(self, node):
#    self.out.append('\\ref{fig:%s}' % node['target'])
    raise nodes.SkipNode
def latex_depart_figref(self, node):
    raise nodes.SkipNode
LaTeXTranslator.visit_figref = latex_visit_figref
LaTeXTranslator.depart_figref = latex_depart_figref

# --- latex math ---------------------------------------------------------------
def latex_visit_math(self, node):
    self.out.append('$%s$\n' % node['latex'])
    raise nodes.SkipNode
LaTeXTranslator.visit_math = latex_visit_math

# --- latex displaymath -------------------------------------------------------
def latex_visit_displaymath(self, node):
    self.out.append('$$%s$$\n' % node['latex'])
    raise nodes.SkipNode
LaTeXTranslator.visit_displaymath = latex_visit_displaymath

# --- latex abstract -----------------------------------------------------------
def latex_visit_abstract(self, node):
    raise nodes.SkipNode
LaTeXTranslator.visit_abstract = latex_visit_abstract

# --- latex keywords -----------------------------------------------------------
def latex_visit_keywords(self, node):
    raise nodes.SkipNode
LaTeXTranslator.visit_keywords = latex_visit_keywords

# --- latex citation  ----------------------------------------------------------
def latex_visit_citation(self, node):
    raise nodes.SkipNode
def latex_depart_citation(self, node):
    raise nodes.SkipNode
#LaTeXTranslator.visit_citation = latex_visit_citation
#LaTeXTranslator.depart_citation = latex_depart_citation

# --- latex citation reference --------------------------------------------------
def latex_visit_citation_reference(self, node):
    raise nodes.SkipNode
#LaTeXTranslator.visit_citation_reference = latex_visit_citation_reference

# --- latex label ---------------------------------------------------------------
def latex_visit_label(self, node):
    raise nodes.SkipNode
#LaTeXTranslator.visit_label = latex_visit_label

# --- latex caption -------------------------------------------------------------
#
# Add a number to figure caption
#
def latex_visit_caption(self, node):
    raise nodes.SkipNode
def latex_depart_caption(self, node):
    raise nodes.SkipNode
#LaTeXTranslator.visit_caption = latex_visit_caption
#LaTeXTranslator.depart_caption = latex_depart_caption


# --- latex no sectnum ---------------------------------------------------------
#
# Indicate current section must not be numbered
#
def latex_visit_nosectnum(self, node):
    raise nodes.SkipNode
def latex_depart_nosectnum(self, node):
    raise nodes.SkipNode
LaTeXTranslator.visit_nosectnum = latex_visit_nosectnum
LaTeXTranslator.depart_nosectnum = latex_depart_nosectnum


# --- latex video --------------------------------------------------------------
def latex_visit_video(self, node):
    raise nodes.SkipNode
def latex_depart_video(self, node):
    raise nodes.SkipNode
LaTeXTranslator.visit_video = latex_visit_video
LaTeXTranslator.depart_video = latex_depart_video



from docutils.core import publish_cmdline, default_description
description = ('Generates (X)LaTeX documents from standalone reStructuredText '
               'sources.  ' + default_description)
publish_cmdline(writer_name='latex', description=description)

