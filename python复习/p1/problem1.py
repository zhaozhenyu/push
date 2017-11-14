
## REMEMBER THAT THIS FILE MUST NOT CONTAIN ANYTHING OTHER THAN YOUR
## FUNCTION DEFINITION, IMPORT STATEMENTS AND COMMENTS. You can use
## docstrings to document your functions, but a docstring should only
## be used inside a function definition, an then only at the very
## beginning of the function suite. Everywhere else you should use
## comments.

## Modify the following function definition so that it computes and
## returns the correct answer to the problem. (The statement "return 0"
## is just a placeholder: you should replace it.)
def approximate_integral(lower, upper, nterms):
    d = abs(upper - lower)/nterms
    a=[]
    S=0
    if nterms==1 :
        lower = lower ** 3
        upper = upper ** 3
        r = (lower + upper) * d / 2
        return r
    else:
        z=lower
        s=0
        for i in range(nterms):
            if i==0:
                lower = lower ** 3
                s=(z+d)**3
                r = (lower +s) * d / 2
                a.append(r)
            else:
                z+=d
                z2=z+d
                r = (z**3 + z2**3) * d / 2
                a.append(r)
    for i in a :
        S+=i
    return S
# print(approximate_integral(-2, -1, 2))