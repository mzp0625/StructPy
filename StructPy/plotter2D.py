#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 22:40:43 2018

@author: mma
"""

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

def window(name, size):
    return plt.figure(name, figsize = size)

def undeformed2D(model, nodal_load, size = (5,5)):
    """
        Plots the structural model in its undeformed shape, with applied nodal forces
    """
    undeformed2D = window('Undeformed Shape', size)
    axes = undeformed2D.add_subplot(111, aspect = 'equal')
    axes.set_xlabel('X')
    axes.set_ylabel('Y')
    axes.set_title("Undeformed Shape", fontsize = 16)

    # plots nodes & nodal forces
    axes.scatter(model.XYZ[:,0],model.XYZ[:,1],marker = 's', c = 'k')
    range_X = max(model.XYZ[:,0])-min(model.XYZ[:,0])
    range_Y = max(model.XYZ[:,1])-min(model.XYZ[:,1])
    arrow_size = (np.mean([range_X, range_Y]))/20
    for node, P in nodal_load.items():
        if P[0] != 0:
            axes.arrow(model.XYZ[node-1][0], model.XYZ[node-1][1], arrow_size, 0, 
                       width = arrow_size/10, color = 'r')
        if P[1] != 0:
            axes.arrow(model.XYZ[node-1][0], model.XYZ[node-1][1], 0, arrow_size, 
                       width = arrow_size/10, color = 'r')
        
    # labels nodes & nodal forces
    for node, xyz in enumerate(model.XYZ):
        axes.text(xyz[0], xyz[1], str(node + 1), color = 'b', size = '10')
        
    for node, p in nodal_load.items():    
        if nodal_load[node][0] != 0:
            axes.text(model.XYZ[node-1][0] + 2 * arrow_size, model.XYZ[node-1][1], nodal_load[node][0], color = 'r', size = '10')
        if nodal_load[node][1] != 0:
            axes.text(model.XYZ[node-1][0], model.XYZ[node-1][1] + 2 * arrow_size, nodal_load[node][1], color = 'r', size = '10')
    
    # plots members     
    CONN = model.CONN - 1 # Modify connectivity matrix to conform to Python indexing that starts at 0
    XYZ = model.XYZ
    for conn in CONN:
        x = [XYZ[conn[0]][0], XYZ[conn[1]][0]]
        y = [XYZ[conn[0]][1], XYZ[conn[1]][1]]
        line = Line2D(x, y, linewidth = 1.0, color = 'black')
        axes.add_line(line)        
    
    # labels members
    for e, conn in enumerate(CONN):
        xm = (XYZ[conn[0]][0] + XYZ[conn[1]][0])/2
        ym = (XYZ[conn[0]][1] + XYZ[conn[1]][1])/2
        axes.text(xm, ym, str(e + 1), color = 'g', size = '10')
        
    # reset x, y limit
    axes.set_xlim(min(XYZ[:,0]) - 2*arrow_size, max(XYZ[:,0] + 3*arrow_size))
    axes.set_ylim(min(XYZ[:,1]) - 2*arrow_size, max(XYZ[:,1] + 3*arrow_size))
    
    print('Nodal Restraints: \n')
    for i, bound in enumerate(model.BOUND):
        if (bound[0] and bound[1]) == 1:
            print('node ' + str(i+1) + ':' + ' X,Y')
        elif (bound[0] == 1 and bound[1] == 0):
            print('node ' + str(i+1) + ':' + ' X')
        elif (bound[0] == 0 and bound[1] == 1):
            print('node ' + str(i+1) + ':' + ' Y')
                    
    
def deformed2D(model, U, scale = 1, size = (5,5)):
    """
        Plots the structural model in its deformed shape
        U : Nodal displacements
        scale : Scale factor
    """
    deformed2D = window('Deformed Shape', size)
    axes = deformed2D.add_subplot(111, aspect = 'equal')
    axes.set_xlabel('X')
    axes.set_ylabel('Y')
    axes.set_title("Deformed Shape with scale = " + str(scale), fontsize = 16)
    
    
    # plots nodes in their undeformed & deformed positions
    XYZ = model.XYZ.copy()
    for i in range(len(XYZ)):
        XYZ[i] = [XYZ[i,0] + U[2*i]*scale, XYZ[i,1] + U[2*i + 1]*scale]
    
    axes.scatter(XYZ[:,0],XYZ[:,1],marker = 's', c = 'k', alpha = 1) # deformed
    axes.scatter(model.XYZ[:,0],model.XYZ[:,1],marker = 's', c = 'k', alpha = 1) # undeformed
    range_X = max(XYZ[:,0])-min(XYZ[:,0])
    range_Y = max(XYZ[:,1])-min(XYZ[:,1])
    
    # labels nodes
    for node, xyz in enumerate(model.XYZ):
        axes.text(xyz[0], xyz[1], str(node + 1), color = 'b', size = '10')
        
    
    # plots members in their undeformed & deformed positions   
    CONN = model.CONN - 1 # Modify connectivity matrix to conform to Python indexing that starts at 0
    for conn in CONN: # deformed
        xd = [XYZ[conn[0]][0], XYZ[conn[1]][0]]
        yd = [XYZ[conn[0]][1], XYZ[conn[1]][1]]
        line = Line2D(xd, yd, linewidth = 1.0, color = 'orange')
        axes.add_line(line)
    for conn in CONN: # undeformed
        xu = [model.XYZ[conn[0]][0], model.XYZ[conn[1]][0]]
        yu = [model.XYZ[conn[0]][1], model.XYZ[conn[1]][1]]
        line = Line2D(xu, yu, linewidth = 1.0, color = 'black')
        axes.add_line(line)   
    # labels members
    for e, conn in enumerate(CONN):
        xm = (XYZ[conn[0]][0] + XYZ[conn[1]][0])/2
        ym = (XYZ[conn[0]][1] + XYZ[conn[1]][1])/2
        axes.text(xm, ym, str(e + 1), color = 'g', size = '10')

    # reset x, y limit
    axes.set_xlim(min(XYZ[:,0]) - range_X/5, max(XYZ[:,0] + range_X/5))
    axes.set_ylim(min(XYZ[:,1]) - range_Y/5, max(XYZ[:,1] + range_Y/5))
    
def axial_Force2D(model, Q, size = (5,5)):
    """
        Plots the structural model in its undeformed shape, with element axial forces
    """
    axial2D = window('Axial Force', size)
    axes = axial2D.add_subplot(111, aspect = 'equal')
    axes.set_xlabel('X')
    axes.set_ylabel('Y')
    axes.set_title("Axial Force", fontsize = 16)

    # plots nodes 
    axes.scatter(model.XYZ[:,0],model.XYZ[:,1],marker = 's', c = 'k')
    range_X = max(model.XYZ[:,0])-min(model.XYZ[:,0])
    range_Y = max(model.XYZ[:,1])-min(model.XYZ[:,1])
        
    # labels nodes
    for node, xyz in enumerate(model.XYZ):
        axes.text(xyz[0], xyz[1], str(node + 1), color = 'b', size = '10')
        
    # plots members     
    CONN = model.CONN - 1 # Modify connectivity matrix to conform to Python indexing that starts at 0
    XYZ = model.XYZ
    for conn in CONN:
        x = [XYZ[conn[0]][0], XYZ[conn[1]][0]]
        y = [XYZ[conn[0]][1], XYZ[conn[1]][1]]
        line = Line2D(x, y, linewidth = 1.0, color = 'black')
        axes.add_line(line)        
    
    # labels members forces
    for i, conn in enumerate(CONN):
        xm = (XYZ[conn[0]][0] + XYZ[conn[1]][0])/2
        ym = (XYZ[conn[0]][1] + XYZ[conn[1]][1])/2
        axes.text(xm, ym, str(round(Q[i])), color = 'g', size = '10')
        
    # reset x, y limit
    axes.set_xlim(min(XYZ[:,0]) - range_X/5, max(XYZ[:,0] + range_X/5))
    axes.set_ylim(min(XYZ[:,1]) - range_Y/5, max(XYZ[:,1] + range_Y/5))
    
def shear_Force2D(model, Q):
    """
        Plots the structural model in its undeformed shape, with element shear forces
    """
    raise Exception("This feature has not bee implemented yet!")

def bending_Moment2D(model,Q):
    """
        Plots the structural model in its undeformed shape, with bending moments
    """
    raise Exception("This feature has not bee implemented yet!")