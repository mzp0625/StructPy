#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 23:36:19 2018

Element Object, contains the following classes: 
    
    elemData()
    
@author: mma
"""

import numpy as np
import math

class elemData():
    
    def __init__(self):
        
        """
            Initializes element properties
            
            E = Elastic Modulus
            A = Cross-sectional Area
            I = Second Moment of Area about axis of bending
            TYPE = element type. "TRUSS" or "FRAME"
        """
        self.E = {}
        self.A = {}
        self.I = {}
        self.TYPE = {}
    
    def localize(self, model, e):
        """
            Returns:
                
            xyz : global coordinates of eth element in structural model
            dof : degrees of freedom the element contributes to
        """
        
        xyz = model.XYZ[model.CONN[e,:]-1]        
        
        dof = model.DOF[model.CONN[e,:]-1]
        
        return xyz, dof
    
    def elemLength(self, xyz):
        """
            Returns:
                
            L : element length
            d_cos : directional cosine with respect to x-axis
                [dX/L, dY/L, dZ/L]
        """
        
        d_xyz = xyz[1,:] - xyz[0,:]
        
        L = math.sqrt(np.dot(np.transpose(d_xyz), d_xyz))
        
        d_cos = d_xyz/L
        
        return L, d_cos
        
        
    