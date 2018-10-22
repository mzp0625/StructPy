#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 16:29:07 2018

@author: mma
"""
from StructPy import Element, Model, DispMethod, plotter2D

import numpy as np

"""
Pratt Truss with 8 bays
"""

# Structure Geometry Data

# Nodal Position & Nodal load definition
XYZ = np.zeros([16,3])
for i in range(9):
    XYZ[i] = [i*100, 0, 0]
for i in range(9,16):
    XYZ[i] = [(i-8)*100, 100, 0]

nodal_load = {13:[0.,-100.]}

# Connectivity
CONN = np.zeros([29,2]).astype(np.int64)
for i in range(8):
    CONN[i] = [i+1,i+2]
for i in range(23,29):
    CONN[i] = [i-13, i-12]
CONN[8:23,:] = [[1,10],
                [2,10],
                [3,10],
                [3,11],
                [4,11],
                [4,12],
                [5,12],
                [5,13],
                [5,14],
                [6,14],
                [6,15],
                [7,15],
                [7,16],
                [8,16],
                [9,16]]

# Boundary Condition
BOUND = np.zeros([16,3]).astype(np.int64)
BOUND[0] = [1,1,0]
BOUND[8] = [1,1,0]

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
