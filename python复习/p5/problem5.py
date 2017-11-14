
## REMEMBER THAT THIS FILE MUST NOT CONTAIN ANYTHING OTHER THAN YOUR
## FUNCTION DEFINITION, IMPORT STATEMENTS AND COMMENTS. You can use
## docstrings to document your functions, but a docstring should only
## be used inside a function definition, an then only at the very
## beginning of the function suite. Everywhere else you should use
## comments.

## Modify the following function definition so that it computes and
## returns the correct answer to the problem. (The statement "return 0"
## is just a placeholder: you should replace it.)

def digit_sum(number):
    k=str(number)
    z=[]
    S=0
    for i in k:
        S+=int(i)
        z.append(i)
    print(z,S,'ssss')
    return S
# digit_sum(1)