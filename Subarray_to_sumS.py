#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
'''
Let A be an array of n integers. With the ordered pair (i; j), 0 <= i <= j < n, we represent
we present its subarray starting from the element in position i and ending with
the element in position j, we define value of a subarray as the sum of its elements.
Design an algorithm that, given an array A of positive integers and one positive integer
s, returns the sorted pair representing the leftmost subarray of A
which has value s. If such a subarray doesn't exist, the function should return None.
The algorithm must have computational cost O(n).
For example, for A = [1; 3; 5; 2; 9; 3; 3; 1; 6]
• with s = 7 the algorithm must return the pair (2; 3)[index (there are in fact in A three subarrays with value 7 whose pairs in order from left to right are
(2; 3); (5; 7); (7; 8)).
• with s = 21 the algorithm must return None as A has no subarray with value 21 .
  
'''


### INPUT: Array of n undistinguished and not sorted integers with ordered pair (i,j), integer s
## OUTPUT: the leftmost pair such that A[i]+A[j]==s
  
A = [1, 3, 5, 2, 9, 3, 3, 1, 6] # example: s=8
  
def subarray_to_sumS(A,s):
    ''' i e j possono essere lo stesso elemento'''
    i,j=(0,0 ) # both indexs start at zero
    sum=0
    
    while j<len(A):
      print(i,j)
      sum+=A[j]
      while sum > s: # until the sum is greater than S, I subtract the element in position i and advance the index
        sum-=A[i]
        i+=1
      if sum==s:return (i,j) # I need the leftmost ordered pair, whose sum is S-input, the first is enough for me,then I can  to exit 
      j+=1
    return None #if the while loop terminates it means that I have no pairs sorted
                #   as S-input sum subarray


if __name__=='__main__':
   print(subarray_to_sumS(A,7))
   