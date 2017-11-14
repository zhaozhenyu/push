
## REMEMBER THAT THIS FILE MUST NOT CONTAIN ANYTHING OTHER THAN YOUR
## FUNCTION DEFINITION, IMPORT STATEMENTS AND COMMENTS. You can use
## docstrings to document your functions, but a docstring should only
## be used inside a function definition, an then only at the very
## beginning of the function suite. Everywhere else you should use
## comments.

## Modify the following function definition so that it computes and
## returns the correct answer to the problem. (The statement "return {}"
## is just a placeholder: you should replace it.)

def count_dict_difference(A, B):
    k = {}
    A_set=set()
    B_set = set()
    for i in A:
        A_set.add(i)
    for j in B:
        B_set.add(j)
    A_list_difference= list(A_set.difference(B_set))
    list_A_union_B= list(A_set.intersection(B_set))
    for i in A_list_difference: ## unique items in A
        k.setdefault(i,A[i])
    for i in  list_A_union_B:
        Value = A[i] - B[i]
        if Value>0 :
            k.setdefault(i, Value)
    return k
