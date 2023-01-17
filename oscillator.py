# ----------------------------------------------------------------------------
# DiSCUS - oscillator file
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

import scipy
from scipy import integrate
from Imports.parameters import *


#########################################################################################
### Program (oscillator) functions ######################################################
# Define rates										
v = scipy.zeros((4),'d')								
def rate_eqs(S):									
    v[0] = delta * (xix*((1+ro*S[0]**2)/(1+S[0]**2 + sigma*S[1]**2)) - S[0])	
    v[1] = delta * gamma * ((1+ro*S[0]**2)/(1+S[0]**2)) - S[1]			
    return v									
																				
# Define ODEs										
def diff_eqs(S,t):									
    Sdot = scipy.zeros((2),'d')							
    v = rate_eqs(S)									
    Sdot[0] = v[0]# dx/dt								
    Sdot[1] = v[1]# dy/dt								
    return Sdot									
											
# Initialise variables and parameters
delta = 10.35; epsilon = 0.05; ro = 50.0; sigma = 1.0; xix = 1.58; gamma = 0.0767	
x = 0.0; y = 0.0									
											
def calculateOsc(x,y):
### Function to integrate a set of ODEs
### In: molecular species
### Out: integration of the ODEs in the time interval defined			
    t_tot = 0.0									
    t_start = 0.0; t_end = i_time; t_inc = 0.01					
    t_range = scipy.arange(t_start,t_end,t_inc)					
    t_course = scipy.integrate.odeint(diff_eqs,[x,y],t_range)			
    x = t_course[-1][0]								
    y = t_course[-1][1]								
    return [x, y]									
											

