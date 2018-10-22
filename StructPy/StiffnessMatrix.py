#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 22:46:31 2018

@author: mma
"""

import numpy as np
from scipy.linalg import block_diag
def create_k_Matrix(TYPE, Elem, e, L):
    """
        Creates basic element stiffness matrix k
        where k is a numpy matrix whose size depends on element type
    """
    EA = Elem.E[e] * Elem.A[e]
    if TYPE == "TRUSS":
        k = np.matrix(EA/L)
    elif TYPE == "FRAME":
        raise Exception("Frame element has not been implemented yet!")
    return k

def create_Ks_Matrix(model, Elem):
    """
        Creates block-diagonal deformation-force matrix Ks
        
    """
    ks = []
    for e in range(model.ne):
        
        xyz, dof = Elem.localize(model,e)
        
        L, dcos = Elem.elemLength(xyz)
        
        ks.append(create_k_Matrix(model.TYPE[e], Elem, e, L))
    
    Ks = block_diag(*ks)
    
    return Ks

def create_Kff_Matrix(model,Af, Ks):
    """
        Returns Kff, the stiffness matrix for the free DOFs
    """
    Kff = Af.T@Ks@Af
    return Kff