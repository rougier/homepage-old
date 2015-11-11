#!/usr/bin/env python

#------------------------------------------------------------------------------
#
#   Copyright (c) 2007 Nicolas Rougier
# 
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
# 
#------------------------------------------------------------------------------
#
# This program demonstrates how to make an OpenGL offscreen rendering using
# FBO (FrameBuffer Object) and how to save the image to disk. It requires glew
# for accessing OpenGL extensions.
#
#------------------------------------------------------------------------------

import sys, Image
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pyglew import *

def display():
    """ Display function """
    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    color = [1.0,0.,0.,1.]
    glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
    glutSolidSphere(2, 20, 20)
    glPopMatrix()
    glutSwapBuffers()

def reshape(width, height):
    """ Reshape function """
    
    glViewport (0, 0, width, height)
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity()
    gluPerspective (40.,width/float(height),1.,40.)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt (0,0,10, 0,0,0, 0,1,0)

def screenshot (filename, size = None):
    """ Offscreen rendering
    
    Save an offscreen rendering of size (w,h) to filename.
    """
    
    def round2 (n):
        """ Get nearest power of two superior to n """
        f = 1
        while f<n:
            f*= 2
        return f

    if size == None:
        size = (512,512)
    w = round2 (size[0])
    h = round2 (size[1])

    image = Image.new ("RGB", (w, h), (0, 0, 0))
    bits = image.tostring("raw", "RGBX", 0, -1)

    # Setup framebuffer
    framebuffer = glGenFramebuffersEXT (1)
    glBindFramebufferEXT(GL_FRAMEBUFFER_EXT, framebuffer)

    # Setup depthbuffer
    depthbuffer = glGenRenderbuffersEXT (1)
    glBindRenderbufferEXT (GL_RENDERBUFFER_EXT,depthbuffer)
    glRenderbufferStorageEXT (GL_RENDERBUFFER_EXT, GL_DEPTH_COMPONENT, w, h)
    
    # Create texture to render to
    texture = glGenTextures (1)
    glBindTexture (GL_TEXTURE_2D, texture)
    glTexParameteri (GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri (GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D (GL_TEXTURE_2D, 0, GL_RGB, w, h, 0,
                    GL_RGB, GL_UNSIGNED_BYTE, bits)
    glFramebufferTexture2DEXT (GL_FRAMEBUFFER_EXT, GL_COLOR_ATTACHMENT0_EXT,
                               GL_TEXTURE_2D, texture, 0);
    glFramebufferRenderbufferEXT(GL_FRAMEBUFFER_EXT, GL_DEPTH_ATTACHMENT_EXT, 
                                 GL_RENDERBUFFER_EXT, depthbuffer);
                                
    status = glCheckFramebufferStatusEXT (GL_FRAMEBUFFER_EXT);
    if status != GL_FRAMEBUFFER_COMPLETE_EXT:
        print "Error in framebuffer activation"
        return

    # Render & save
    reshape (size[0],size[1])
    display()
    data = glReadPixels (0, 0, w, h, GL_RGB,  GL_UNSIGNED_BYTE)
    image.fromstring (data)
    image = image.crop ((0,0,size[0], size[1]))
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    image.save (filename)

    # Cleanup
    glBindRenderbufferEXT (GL_RENDERBUFFER_EXT, 0)
    glBindFramebufferEXT (GL_FRAMEBUFFER_EXT, 0)
    glDeleteTextures (1,[texture])
    glDeleteFramebuffersEXT (1, [framebuffer])


def keyboard (keycode, x, y):
    """ Keyboard function """
    
    if (keycode == 'q'):
        sys.exit()
    elif (keycode == ' '):
        screenshot ("screenshot.png")

def init():
    """ Init function """
    
    glClearColor(0,0,0,1)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    lightPosition = [10,4,10,1]
    lightColor = [1.0, 1.0, 1.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, lightPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)


if (__name__ == '__main__'):
   glutInit (sys.argv)
   glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
   glutInitWindowSize (512,512)
   glutCreateWindow ("Offscreen rendering using FBO")
   glewInit()
   init()
   glutDisplayFunc(display)
   glutReshapeFunc(reshape)
   glutKeyboardFunc(keyboard)
   glutMainLoop()
