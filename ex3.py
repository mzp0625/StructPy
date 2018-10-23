#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 16:29:07 2018

@author: mma
"""
from StructPy import Element, Model, DispMethod, plotter2D

import numpy as np

"""
Hanger Structure
"""

# Structure Geometry Data

# Nodal Position & Nodal load definition
x1 = np.linspace(-90,90,19)
x2 = np.linspace(-80,80,19)
y1 = 60 - 0.00741 * np.square(x1)
y2 = 50 - 0.00781 * np.square(x2)

XYZ = np.zeros([38 , 3])

XYZ[0:19,0] = x1
XYZ[0:19,1] = y1
XYZ[19:,0] = x2
XYZ[19:,1] = y2

nodal_load = {10:[100.,0.], 29 :[100,0]}

# Connectivity

CONN = np.zeros([71,2]).astype(np.int64)
for i in range(18):
    CONN[i] = [i+1, i+2]
for i in range(18,36):
    CONN[i] = [i+2, i+3]
for i in range(36, 45):
    CONN[i] = [i-34, i-16]
for i in range(45,54):
    CONN[i] = [i-35, i-15]
for i in range(54,71):
    CONN[i] = [i-52, i-33]
    
# Boundary Condition
BOUND = np.zeros([38,3]).astype(np.int64)
BOUND[0] = [1,1,0]
BOUND[19] = [1,1,0]
BOUND[20] = [1,1,0]
BOUND[37] = [1,1,0]

# Element Material Data
n = len(CONN) # number of elements
Elem = Element.elemData()

for i in range(n):
    Elem.E[i] = 10000.
    Elem.A[i] = 20.
    Elem.I[i] = 1000.
    Elem.TYPE[i] = 'TRUSS'
    
# Create model    
model = Model.CreateModel(Elem, XYZ, CONN, BOUND)
# Nodal displacement U, element force Q
U,Q = DispMethod.solver(model, Elem, nodal_load)

# Plots structure and forces
size = (15,10)
scale = 20
undeformed = plotter2D.undeformed2D(model, nodal_load, size)
deformed = plotter2D.deformed2D(model,U, scale,size)
axialForce = plotter2D.axial_Force2D(model, Q, size)
