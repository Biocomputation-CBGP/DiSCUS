# ----------------------------------------------------------------------------
# DiSCUS - cross example file
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



##################################################################################
### This example simulates two bacterial strains (1- donors with an oscillator as
### the inside circuit; 2- recipients) in a cross-shaped channel. Transconjugants
### receive successfuly the plasmid containin the genetic oscillator
##################################################################################





from Imports.definitions import *
from Imports.cell_class import *
from discus import *


def add_walls(space):
### Function used to place the walls in the world (walls scaled depending on screenview)
### In: the space
### Out: returns the shapes (l) of the walls
    body = pymunk.Body()
    body.static = True
    body.position = (0.39*screenview,0.39*screenview)    
    l1 = pymunk.Segment(body, (-0.39*screenview, 0), (0.0, 0.0), 5.0)
    l2 = pymunk.Segment(body, (0.0, 0), (0.0, -0.39*screenview), 5.0)
    body = pymunk.Body()
    body.static = True
    body.position = (screenview - 0.39*screenview,0.39*screenview)    
    l3 = pymunk.Segment(body, (0, 0), (0.39*screenview, 0.0), 5.0)
    l4 = pymunk.Segment(body, (0.0, 0), (0.0, -0.39*screenview), 5.0)
    body = pymunk.Body()
    body.static = True
    body.position = (0.39*screenview,screenview - 0.39*screenview)    
    l5 = pymunk.Segment(body, (-0.39*screenview, 0), (0.0, 0.0), 5.0)
    l6 = pymunk.Segment(body, (0.0, 0), (0.0, 0.39*screenview), 5.0)
    body = pymunk.Body()
    body.static = True
    body.position = (screenview - 0.39*screenview,screenview - 0.39*screenview)    
    l7 = pymunk.Segment(body, (0, 0), (0.0, 0.39*screenview), 5.0)
    l8 = pymunk.Segment(body, (0.0, 0), (0.39*screenview, 0.0), 5.0)
    space.add(l1, l2, l3, l4, l5, l6, l7, l8)
    return l1,l2,l3,l4,l5,l6,l7,l8

screenview = 300 			### Scren size 
screen = pygame.display.set_mode((screenview, screenview))
clock = pygame.time.Clock()
space = pymunk.Space()
bacs = []
walls = add_walls(space)

### Loop for the placement of recipients in the world
### considering the cross-shaped defined by the definition add_walls
for i in range(number_recipients):
    points = [(0, -width), (0, width), (length,width), (length, -width)]
    r_y = random.uniform(0.48*screenview, screenview-0.48*screenview)
    r_x = random.uniform(6*screenview/8,7*screenview/8)
    r_angle = random.randint(0,360)
    bac_shape = add_bac(space,r_x,r_y, math.radians(r_angle), points)
    b = bacteria(bac_shape,[0,0],[0,0],[bac_shape.body.position.x, bac_shape.body.position.y], 0, False, False,1,0)
    bacs.append(b)
    
### Loop for the placement of donors in the world
### considering the cross-shaped defined by the definition add_walls
for i in range(number_donors):
    points = [(0, -width), (0, width), (length,width), (length, -width)]
    r_y = random.uniform(0.48*screenview, screenview-0.48*screenview)
    r_x = random.uniform(screenview/8, 2*screenview/8)
    r_angle = random.randint(0,360)
    bac_shape = add_bac(space,r_x,r_y, math.radians(r_angle), points)
    b = bacteria(bac_shape,[x,y],[0,0],[bac_shape.body.position.x, bac_shape.body.position.y], 0, False, True,0,0)
    bacs.append(b)

def main():
    discus(screenview, screen, clock, bacs, space, walls)
if __name__ == '__main__':  
    main()
