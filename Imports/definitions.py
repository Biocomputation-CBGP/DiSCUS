# ----------------------------------------------------------------------------
# DiSCUS - definitions file
# http://code.google.com/p/discus/
# Angel Goni-Moreno - www.angelgm.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ----------------------------------------------------------------------------


import pymunk
from parameters import *
import pygame
from pygame.locals import *
from pygame.color import *

def add_bac(space,x,y,angle,points):
### Function used to place a new cell in the world.
### In: the space into which a bacteria must be created, its coordinates and angle.
### Out: returns a shape with a body assigned
    mass = bac_mass
    moment = pymunk.moment_for_poly(mass, points, (0,0))
    body = pymunk.Body(mass, moment)
    body.position = x, y
    body.angle =  angle
    shape = pymunk.Poly(body, points, (0,0))
    shape.friction = bac_friction
    space.add(body,shape)
    return shape

def get_centres(points):
### Function used to obtain the centres of daughter cells in division
### In: four points of a rectangle
### Out: returns the middle point and the centre of the left side
    centre = ((points[2][0]+points[7][0])/2, (points[2][1]+points[7][1])/2)
    centre_left =  points[2]
    return (centre_left, centre)

def hex_to_rgb(value):
### Function used to convert an hexagonal value into a rgb value
### In: hexagonal value
### Out: RGB value
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))

def draw_bac(screen, bac):
### Function used to draw a cell in the screen for live video
### In: the cell and the screen in which it must be draw 
### Out: popup window with live video
    body = bac.shape.body
    ps = bac.shape.get_vertices()
    color = THECOLORS["green"]
    if bac.program == None: cell_color = THECOLORS["yellow"]
    else: cell_color = hex_to_rgb(calculateColor(bac.program[0]))
    pygame.draw.polygon(screen, cell_color, ps)
    pygame.draw.polygon(screen, THECOLORS["black"], ps,1)

def draw_lines(screen, lines):
### Function used to draw the walls in the screen for live video
### In: the lines and the screen into which they must be drawn
### Out: popup window with live video
    for line in lines:
        body = line.body
        pv1 = body.position + line.a.rotated(body.angle)
        pv2 = body.position + line.b.rotated(body.angle)
        pygame.draw.lines(screen, THECOLORS["black"], False, [pv1,pv2])

def look_mate(mate_shape, bacs):
### Function used to look for a shape in a list of cells
### In: a shape and a list of cells
### Out: the cell found or None
    for bac in bacs:
        if bac.shape == mate_shape: return bac

def look_bac(body, bacs):
### Function used to look for a body in a list of cells
### In: a body and a list of cells
### Out: the cell found or None
    for bac in bacs:
        if bac.shape.body == body: return bac

def calculateGravity(bx, by):
### Function add gravity towards a specific point
### In: coordinates of the cell
### Out: new coordinates according to the gravity defined
    centre_sc = (screenview/2, screenview/2)
    if bx > centre_sc[0]:
        gr_x = -0.045
    else:
        gr_x = 0.045
    if by > centre_sc[1]:
        gr_y = -0.045
    else:
        gr_y = 0.045
    return (gr_x,gr_y)

def calculateColor(x):
### Function to calculate gradual colour according to a value				
### In: the value to associate a colour
### Out: the hexadecimal green colour proportional 
    initial_color = '#000000'					
    if x == 0:				
        final_color = '#001000'			
    elif x>0 and x<10:								
        final_color = '#002800'							
    elif x>=10 and x<20:								
        final_color = '#004000'							
    elif x>=20 and x<30:								
        final_color = '#006000'							
    elif x>=30 and x<40:								
        final_color = '#007800'							
    elif x>=40 and x<50:								
        final_color = '#009800'							
    elif x>=50 and x<60:								
        final_color = '#00B800'							
    elif x>=60 and x<70:								
        final_color = '#00D800'							
    elif x >= 70:									
        final_color = '#00F800'							
    return final_color
