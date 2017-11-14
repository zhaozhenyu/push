
## REMEMBER THAT THIS FILE MUST NOT CONTAIN ANYTHING OTHER THAN YOUR
## FUNCTION DEFINITION, IMPORT STATEMENTS AND COMMENTS. You can use
## docstrings to document your functions, but a docstring should only
## be used inside a function definition, an then only at the very
## beginning of the function suite. Everywhere else you should use
## comments.

import numpy as np

## Modify the following function definition so that it computes and
## returns the correct answer to the problem. (The return statement
## is just a placeholder: you should replace it.)
from itertools import islice


def moving_average(seq, wsize):
    l=[]
    for i in range(len(seq)+1-wsize):
        print(seq[i:i + wsize] / wsize  ,'''sssss''')
        l.append(sum(seq[i:i+wsize]/wsize))
    return np.array(l)
