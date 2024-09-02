"""
Tensor Basics-

Constructing a tensor: 
torch.empty()
torch.zeros()
torch.ones()
torch.rand()
torch.tensor([1,2]) # actual tensor 1, 2

Tensor Attributes:
x.dtype 
x.size()

Tensor Operations: 
z = x + y or x - y or x / y or x*y (not in place!)
y.add_(x) (all '_' modify it in place!)

Accessing Elements: 
x[rows, columns]
x[a,b].item() gives you the precise value at one spot.

Resizing Tensor: 
if the dimensions are c = a*b
x.view(c) gives a 1d vector 
x.view(-1, d) gives a d by d/c vector

Converting between Tensor and numpy: 
- both a and b share the same memory space so if you modify a, b is also modified. because we are on CPU.
a = torch.ones(5)
b = a.numpy() # creates a numpy array from the tensor. 
OR 
a = np.ones(5) 
b = torch.from_numpy(a)
"""

import torch
import numpy as np 