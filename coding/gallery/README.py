#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import glob

readme = """
Matplotlib gallery
==================

"""
    
figure_rst = """
.. figure:: %s/%s.png
   :target: %s/%s-large.png

   Source `%s.py <%s/%s.py>`_

"""

directories = 'spine', 'style', 'image', 'grid', 'one-line', 'showcase'
for d in directories:
    print "Making all in", d
    for f in glob.glob(d+"/*.py"):
        name = os.path.basename(f)
        name = name.split('.')[0]
        readme +=  figure_rst % (d,name,d,name,name,d,name)
    print
f = open('README.rst','w')
f.write(readme)
f.close()

