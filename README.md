# StructPy
A Python Structural Analysis Package for linear problems. 

## How to use:

Clone or download from github directory to import StructPy. The StructPy package contains the following modules:

	•	Element.py : 	      defines elemData class and its associated methods localize, elemLength
	•	Model.py : 	      defines Model class and its associated method index_fr
	•	Kinematics.py :	      defines functions create_A_Matrix, create_ag_Matrix, create_Af_Matrix 
	•	Load.py :             defines functions create_P_vector, create_Pf_vector 
	•	StiffnessMatrix.py :  defines functions create_k_Matrix, create_Ks_Matrix, create_Kff_Matrix
	•	DispMethod.py :       defines function solver that applies the displacement method of analysis
	•	plotter2D.py : 	      defines functions window, undeformed2D, deformed2D, axial_Force2D
	•	plotter3D.py : 	      (not yet implemented)


## Features:
	✓	2-D Truss Analysis
	        3-D Truss Analysis
	        2-D Frame Analysis
	        3-D Frame Analysis
	✓	2-D Plotting
	✓	    Undeformed Shape
	✓	    Deformed Shape
	✓	    Axial Force
		    Shear Force
		    Bending Moment
	        3-D Plotting
	        Hinge modeling
	        Distributed Loading
	        Dynamic Loading

## Examples:

### Ex1:

First begin by importing the necessary modules from StructPy:

```
from StructPy import Element, Model, DispMethod, plotter2D

import numpy as np
```

Define the model geometry, where XYZ contains nodal positions, CONN contains connectivity information and BOUND specifies boundary conditions (0 for free and 1 for fixed):

```
# Nodal Position & Nodal load definition
XYZ = np.array([[0,0,0],[1,2,0],[2,0,0]]).astype(np.float32) 

nodal_load = {2:[100.,100.]}

# Connectivity
CONN = np.array([[1,2],[2,3],[1,3]])

# Boundary Condition
BOUND = np.array([[1,1,0],[0,0,0],[0,1,0]])
```
Create Elem object that contains material information on elements:

```
for i in range(n):
    Elem.E[i] = 10000.
    Elem.A[i] = 20.
    Elem.I[i] = 1000.
    Elem.TYPE[i] = 'TRUSS'
```

Create model object and use displacement method to solve for nodal displacements U and element internal forces Q:

```
# Create model    
model = Model.CreateModel(Elem, XYZ, CONN, BOUND)
# Nodal displacement U, element force Q
U,Q = DispMethod.solver(model, Elem, nodal_load)
```

The undeformed and deformed shape, as well as axial forces can then be plotted:
```
undeformed = plotter2D.undeformed2D(model, nodal_load)
```
![ex1_undeformed](https://github.com/mzp0625/StructPy/blob/master/ex1_undeformed.png) 

```
deformed = plotter2D.deformed2D(model,U, scale = 100)
```
![ex1_undeformed](https://github.com/mzp0625/StructPy/blob/master/ex1_deformed.png) 
```
axialForce = plotter2D.axial_Force2D(model, Q)
```
![ex1_undeformed](https://github.com/mzp0625/StructPy/blob/master/ex1_axial.png) 



### Ex2:

A more complicated model can be created by simply changing the geometry numpy arrays XYZ, CONN and BOUND. A simply supported Pratt truss is shown in this example:

```
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
```
![ex1_undeformed](https://github.com/mzp0625/StructPy/blob/master/ex2_undeformed.png) 
![ex1_undeformed](https://github.com/mzp0625/StructPy/blob/master/ex2_deformed.png) 
![ex1_undeformed](https://github.com/mzp0625/StructPy/blob/master/ex2_axial.png) 

### Ex3:
In this example, a 2-D arch structure measuring 180 ft in width and 60 ft in height is analyzed. Again change model geometry through XYZ, CONN and BOUND:

```
# Nodal Position & Nodal load definition
x1 = np.linspace(-90,90,19)
x2 = np.linspace(-80,80,19)
y1 = 60 - 0.00741 * np.square(x1)
y2 = 50 - 0.00781 * np.square(x2)

XYZ = np.zeros([38 , 3])

XYZ[0:19,0] = x1
XYZ[0:19,1] = y1
XYZ[19:,0] = x2
XYZ[19:,1] = y2

nodal_load = {10:[100.,0.], 29 :[100,0]}

# Connectivity

CONN = np.zeros([71,2]).astype(np.int64)
for i in range(18):
    CONN[i] = [i+1, i+2]
for i in range(18,36):
    CONN[i] = [i+2, i+3]
for i in range(36, 45):
    CONN[i] = [i-34, i-16]
for i in range(45,54):
    CONN[i] = [i-35, i-15]
for i in range(54,71):
    CONN[i] = [i-52, i-33]
    
# Boundary Condition
BOUND = np.zeros([38,3]).astype(np.int64)
BOUND[0] = [1,1,0]
BOUND[19] = [1,1,0]
BOUND[20] = [1,1,0]
BOUND[37] = [1,1,0]
```
![ex1_undeformed](https://github.com/mzp0625/StructPy/blob/master/ex3_undeformed.png) 
![ex1_undeformed](https://github.com/mzp0625/StructPy/blob/master/ex3_deformed.png) 
![ex1_undeformed](https://github.com/mzp0625/StructPy/blob/master/ex3_axial.png) 



