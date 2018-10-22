#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 21:07:18 2018

@author: mma
"""
import numpy as np

def create_P_vector(model, nodal_load):
    """
        Creates nodal load vector P based on nodal_load dictionary object
    """
    P = np.zeros(model.nt)
    
    for n, p in nodal_load.items():
        
        if n not in model.CONN:
            
            raise Exception("Load not applied a valid DOF!")
            
        for i, d in enumerate(model.DOF[n-1]):
            
            P[d] = p[i]    
            
    return P

def create_Pf_vector(model, P):
    """
        Creates Pf vector based on index of free degrees of freedom
    """
    idf, idr = model.index_fr()
    
    Pf = P[idf]
    
    return Pf