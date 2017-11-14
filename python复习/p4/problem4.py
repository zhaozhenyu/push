import numpy as np
def unnest(alist):
    k=[] ### append alist to k and k is str type
    flat_list=[]##
    for i in alist:
        k += str(i)
    for i in k:
        if str.isnumeric(i):
            flat_list.append(int(i))
    return flat_list
#
# a=[[2,2,2],[3,3,3],[4,4,4]]
# print(unnest(a))
# z=[]
# print(type(a[0]))
# # for i in a :
#     k+=str(i)
# for i in k:
#     if str.isnumeric(i):
#        z.append(int(i))
# print(z)
# print(c)
# flat_list = [item for sublist in l for item in sublist]
# print (flat_list)