#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 22:40:43 2018

@author: mma
"""

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

def window(name):
    return plt.figure(name)

def undeformed3D(model, nodal_load):
    """
        Plots the structural model in its undeformed shape, with applied nodal forces
    """
    raise Exception("This feature has not bee implemented yet!")
    
def deformed3D(model, U, scale = 1):
    """
        Plots the structural model in its deformed shape
        U : Nodal displacements
        scale : Scale factor
    """
    raise Exception("This feature has not bee implemented yet!")
    
def axial_Force3D(model, Q):
    """
        Plots the structural model in its undeformed shape, with element axial forces
    """
    raise Exception("This feature has not bee implemented yet!")
    
def shear_Force3D(model, Q):
    """
        Plots the structural model in its undeformed shape, with element shear forces
    """
    raise Exception("This feature has not bee implemented yet!")

def bending_Moment3D(model,Q):
    """
        Plots the structural model in its undeformed shape, with bending moments
    """
    raise Exception("This feature has not bee implemented yet!")