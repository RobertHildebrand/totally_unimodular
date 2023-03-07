# Total Unimodularity
This is a simple python script to test if a matrix is totally unimodular (TU).   This runs quickly for reasonably small matrices, but the complexity grows exponentially, so it should not be used on large matrices.  For a better approach (polytime), one should look at the C++ code by Matthias Walter.


## Definition
A matrix is totally unimodular if all square submatrices have determinant +1, -1, or 0.   Note that "all square submatrices" means pick any k columns and any k rows to define a submatrix.

Note that the matrix must have all entries be +1, -1, or 0, by definition, since all entries form 1x1 submatrix.

## Code comments
The code here is a simple implementation that literally checks all possible submatrices.  This can be a lot!  Since the code useses an iterator, it doesn't list all of these matrices in memory, so it might just run for a long time if you hand it a matrix that is too large.  

This code works fine for testing small exmaples (which is usually all that I need to do myself).
But for a better solution, one should really use the fantastic code by Matthias Walter at https://arxiv.org/abs/1202.4061

It would be nice if there was a simple python connection to this code.  Perhaps even a package through pip.


## Why did I post this?
I couldn't find any simple code to do this.  And the one code that I did was actually wrong.  

## Matlab
If you need a matlab implementation, you can download one here https://www.mathworks.com/matlabcentral/fileexchange/40525-totally-unimodular
