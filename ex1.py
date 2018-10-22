#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 21:20:17 2018

@author: mma

"""
from StructPy import Element, Model, DispMethod, plotter2D

import numpy as np

"""
Triangular Simply Supported Truss
"""

# Structure Geometry Data

# Nodal Position & Nodal load definition
XYZ = np.array([[0,0,0],[1,2,0],[2,0,0]]).astype(np.float32) 

nodal_load = {2:[100.,100.]}

# Connectivity
CONN = np.array([[1,2],[2,3],[1,3]])

# Boundary Condition
BOUND = np.array([[1,1,0],[0,0,0],[0,1,0]])

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
undeformed = plotter2D.undeformed2D(model, nodal_load)
deformed = plotter2D.deformed2D(model,U, scale = 100)
axialForce = plotter2D.axial_Force2D(model, Q)

            


