#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 01:19:47 2018

@author: mma
"""
import numpy as np 

class CreateModel():
    """
        Creates structural model
    """
    def __init__(self, Elem, XYZ, CONN, BOUND):
        self.ne = len(CONN) # Number of elements
        self.nn = len(XYZ) # number of nodes
        
        # Load model geometry & properties
        self.XYZ = XYZ
        self.CONN = CONN
        self.BOUND = BOUND
        self.TYPE = list(Elem.TYPE.values())
        
        # Calculate nDim
        if all(self.XYZ[:,2] == 0):
            self.nDim = 2
            
            # Remove Z component if problem is 2-Dimensional
            self.XYZ = self.XYZ[:,0:2]
            self.BOUND = self.BOUND[:,0:2]
        else:
            self.nDim = 3
        
        # Calculate DOF
        self.nq, self.nt, self.nr, self.nf = 0, 0, 0, 0
        # nq = number of element internal forces
        # nt = number of total DOFs
        # nr = number of restrained DOFs
        # nf = number of free DOFs
        
        self.nr = sum(sum(self.BOUND))
        
        ndf = []
        for i in self.TYPE:
            if i == "TRUSS":
                self.nq += 1
            elif i == "FRAME":
                self.nq += 3
        for n in range(self.nn):
            shared_elem = np.where(n == self.CONN)[0]
            if all(np.asarray(self.TYPE)[shared_elem[:]] == 'TRUSS'):
                ndf.append(self.nDim)
            else:
                ndf.append((self.Dim-1)*3)
                
        self.ndf = np.array(ndf)
        self.nt = sum(self.ndf)
        self.nf = self.nt - self.nr
        
        # Instability
        if self.nq - self.nf < 0:
            raise Exception("Structure is unstable!")
                        
        # Initialize Stiffness matrix of free DOFs Kff
        self.Kff = []
        
        DOF = []
        for n, bound in enumerate(self.BOUND):
            DOF.append([n * self.ndf[n] + i for i in range(self.ndf[n])])
        self.DOF = np.array(DOF)
            
        
        
    def index_fr(self):
        """
            Returns:
                ind_f: index of fixed degrees of freedom
                ind_r: index of free degrees of freedom
        """
        idf, idr = [], []
        
        for i in range(np.shape(self.BOUND)[0]):
            for j in range(np.shape(self.BOUND)[1]):
                if self.BOUND[i,j] == 0:
                    idf.append(j + i*(np.shape(self.BOUND)[1]))
                elif self.BOUND[i,j] == 1:
                    idr.append(j + i*(np.shape(self.BOUND)[1]))
        
        return idf, idr
    
            
    
        
            
        
                
        
        
            
        
        
        
            
        
    
    
    
    