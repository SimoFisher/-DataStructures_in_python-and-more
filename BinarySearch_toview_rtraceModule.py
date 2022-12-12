#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
View of recursive calls
"""

## EXAMPLE: To use Class Trace Recursion, with this class, which you need to put in your workspace and import, you can see
## the entry and exit of recursive calls to the function, it is very important to see how it works on the stack, 
### remembering that the last element that allocates is the first to be deallocated according to the LIFO policy,
#### Last in First Out , typical of stacked data structures



def Binary_Search_recursive(lista,x,a,b):
    '''recursive working binary search'''
    if a>b : return 'element x not found'
    # base case
    mid=(a+b)//2
    # midpoint 
    if  lista[mid]==x: return 'found element at index: '+str(mid) +' position'
    if  lista[mid] > x:
        return Binary_Search_recursive(lista,x,a,mid-1)

    else:
        return Binary_Search_recursive(lista,x,mid+1,b)
    
    
## note that for using rtrace module after importing it, you need function_name=rtrace.trace(function_name)
## and finally calls the function with its arguments. 
 
## ACHTUNG -> Remember that integer elements in the list are completely distinct and sorted, on the contrary
## if it didn't, it wouldn't be possible to perform a BinarySearch with log n complexity to search for an element x in the list   
ll=[23,34,55,66,78,88,98,120,150,155,167,201,205]
a=0
b=len(ll)-1
if __name__=='__main__':
    import rtrace
    Binary_Search_recursive=rtrace.trace(Binary_Search_recursive)
    Binary_Search_recursive.trace(ll,201,a,b)    