#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 21:37:42 2018

@author: mma
"""

import numpy as np

def create_A_Matrix(model, Elem):
    """
        Creates and returns A matrix
    """
    A = np.zeros((model.nq, model.nt))
    
    for e in range(model.ne):
        xyz, dof = Elem.localize(model, e)
        
        ag = create_ag_Matrix(model.TYPE[e], xyz, Elem) 
        
        A[e, np.concatenate(dof)] = ag
        
    return A

def create_ag_Matrix(TYPE, xyz, Elem):
    """ 
        Creates and returns local kinematic ag matrix
    """
    L, dcos = Elem.elemLength(xyz)
        
    if TYPE == "TRUSS":
        ag = np.concatenate((-dcos, dcos))
    
    if TYPE ==  "FRAME":
        raise Exception("Frame element has not been implemented yet!")
        
    return ag

def create_Af_Matrix(model, A):
    """
        Creates and returns Af matrix
    """
    idf, idr = model.index_fr()
    
    Af = A[:,idf]
    
    return Af    