#!/usr/bin/env python
# coding: utf-8

# In[37]:


import numpy as np
import itertools

def find_non_unimodular_submatrix(matrix):
    """
    Finds a submatrix of a matrix that is not totally unimodular, and returns the submatrix as well as the row and column indices.
    
    Args:
    matrix: a numpy array representing the matrix.
    
    Returns:
    A tuple (submatrix, rows, cols) where submatrix is the submatrix that is not totally unimodular, and rows and cols are the row and column indices of the submatrix, respectively.
    If the matrix is totally unimodular, returns (None, None, None).
    """
    m, n = matrix.shape

    for k in range(1, m+1):
        for rows in itertools.combinations(range(m), k):
            for cols in itertools.combinations(range(n), k):
                submatrix = matrix[np.ix_(rows, cols)]  # extract the submatrix
                det = np.linalg.det(submatrix)
                if abs(det) != 0 and abs(det) != 1:
                    return submatrix, rows, cols, det  # not totally unimodular
    return None, None, None, None  # totally unimodular

def print_non_unimodular_submatrix(matrix):
    """
    Finds and prints a submatrix of a matrix that is not totally unimodular, as well as the row and column indices.
    If the matrix is totally unimodular, prints a message saying so.
    
    Args:
    matrix: a numpy array representing the matrix.
    """
    submatrix, rows, cols, det = find_non_unimodular_submatrix(matrix)
    if submatrix is not None:
        print("The matrix is not totally unimodular. The following submatrix is not unimodular:")
        print(submatrix)
        print(f"This matrix has determinant: {det}")
        print(f"Row indices: {', '.join(str(row) for row in rows)}")
        print(f"Column indices: {', '.join(str(col) for col in cols)}")
    else:
        print("The matrix is totally unimodular.")

# Example usage:
print("test matrix")
matrix = np.array([[1, 0,0,1, 0,1,1,1], [0, 0,0,1, 1,1,1,1], [1, 0,0,0, 1,1,1,1]])
print(matrix)
print_non_unimodular_submatrix(matrix)


# In[38]:


matrix = np.array([
    [1, 0,0,0,-1,0,-1,0],
    [0,1,0,0,-1,0,0,-1],
    [0,0,1,0,0,-1,-1,0],
    [0,0,0,1,0,-1,0,-1],
     [0,0,0,0,1,1,1,1]])
print(matrix)
print_non_unimodular_submatrix(matrix)


# In[39]:


matrix = np.array([
    [1,0,0,-1,-1,0,0],
    [0,1,0,-1,0,-1,0],
    [0,0,1,-1, 0,0,-1],
     [0,0,0,1,1,1,1]])
print(matrix)
print_non_unimodular_submatrix(matrix)


# In[ ]:




