# ----------------------------------------------------------------------------
# DiSCUS - plain example file
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

###############################################################################
### This exapmle simulates a bacterial strain growing in emtpy space. Thus, the
### walls are defined as NONE. As well as the program (genetic circuit = NONE
###############################################################################


from Imports.definitions import *
from Imports.cell_class import *
from discus import *


screenview = 300 			### Scren size 
screen = pygame.display.set_mode((screenview, screenview))
clock = pygame.time.Clock()
space = pymunk.Space()
bacs = []
walls = None

### Loop for the placement of cells in the world
for i in range(number_recipients):
    points = [(0, -width), (0, width), (length,width), (length, -width)]
    r_y = random.uniform(0, screenview)
    r_x = random.uniform(0, screenview)
    r_angle = random.randint(0,360)
    bac_shape = add_bac(space,r_x,r_y, math.radians(r_angle), points)
    b = bacteria(bac_shape,None,[0,0],[bac_shape.body.position.x, bac_shape.body.position.y], 0, False, False,1,0)
    bacs.append(b)
    
def main():
    discus(screenview, screen, clock, bacs, space, walls)
if __name__ == '__main__':  
    main()
