#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 22:05:57 2018

@author: mma
"""

import numpy as np

from StructPy import Kinematics, Load, StiffnessMatrix

def solver(model, Elem, nodal_load):
    
    A = Kinematics.create_A_Matrix(model, Elem)
    
    Af = Kinematics.create_Af_Matrix(model, A)
    
    Ks = StiffnessMatrix.create_Ks_Matrix(model, Elem)
    
    Kff = StiffnessMatrix.create_Kff_Matrix(model, Af, Ks)
    
    P = Load.create_P_vector(model, nodal_load)
    
    Pf = Load.create_Pf_vector(model, P)
    
    # Solves system of equations Kff*Uf = Pf
    # Assigns Uf to index of free DOFs of U
    Uf = np.linalg.solve(Kff, Pf)
    idf, idr = model.index_fr()
    U = np.zeros(model.nt)
    U[idf] = Uf
    
    # Element internal force Q
    Q = Ks@A@U
    return U,Q

