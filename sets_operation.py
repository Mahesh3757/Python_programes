# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 22:12:50 2024

@author: MAHESH
"""
# Operators used in sets 

a={1,2,3,4}
print("Elements of a =",a)
b={5,6,4,8,9}
print("Elements of b = ",b)
c=a|b
print("Elements of A union B is = ", c)
d=a&b
print("Elements of A intersection of B is =" ,d)
e=a-b
print("Elements of A but not in B =", e)
f=b-a
print("Elements of B but not in A =", f)

#%%
#Operation performed in Sets
#1) all()

a={1,2,3,4,4,3,5,6,10}
print("Elements of a = ",a)
b=all(a)
print("All elements are True or not =", b)
c=any(a)
print("Any elements in the set are true or not = ",c)
d=max(a)
print("Maximum  value of elements in the set is =",d)
e=min(a)
print("Minimum value elements in the sets = ",e)
d=sorted(a)
print("Elements are sorted in the ascending order =",d)
e=sum(a)
print("Sum of all elements in the set is =",e)