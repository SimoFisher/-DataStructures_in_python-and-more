#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 22:00:37 2022

@author: yota
"""

"""A sorted array A of n > 1 distinct integers has undergone
a rotation k positions to the LEFT, 1 ≤ k < n. For example, for 
A =[5, 7, 9, 2, 3] the value of k is 2 ,istead while for A = [9, 2, 3, 5, 7] it is 4.
Design an algorithm that, given the array A, returns the value in O(log n) time
by k.
"""
    
    
 #### In Recursive mode, the simple Algorithmic Idea:
        ### I perform binary searches to find the minimum in time log(n)
        ### as the Array is sorted
        ### we can apply a binary search known to work in log n, always halving the input value, after return len(n)-i
        ### as it returns the number of moves
        ### B=[10,12,15,17,5,7,8,9] len(B)=8 k = 4 rotations
        ### k=len(B) - i rotations
        
        
def recursiveRotations_k(A,i,j):
   
    if A==[] : return 'The List is Empty'
   
    mid = i+j//2 
    if A[mid] > A[mid+1]: 
      # array increasing to a certain point and then decreasing
      # I can check at this point because if the middle element is greater
      # than the next I found the element that was in the last position, 
      # before the rotation.
      return len(A)-(mid+1)
    # at this point I can return the number of moves
    if A[i] < A[mid]:
       
        return recursiveRotations_k(A,mid+1,j)
        # going rigth
    else:
         
        return recursiveRotations_k(A,i,mid)
        # going left
 
def rotation_k_while(A):
    ''' iterative method''' 
    i=mid=0
    j=len(A)-1
    while i<=j:
        mid = round((i+j)/2)
        if A[mid] > A[mid+1]:
                  return len(A)-(mid+1)
                  ## pay attention to the parentheses
                  ## with len(A) -mid+1 is different than written in the above code
            # if it is in ascending order
            # modify the binary search
        
        if A[i] < A[mid]:
            i=mid+1
        else:
            j=mid
            
            

if __name__ == '__main__':
    A = [9, 2, 3, 5, 7]
   
    B=[9,12,15,17,5,7,8,10]
   
    print(recursiveRotations_k(A,0,len(A)-1))
    print(recursiveRotations_k(B,0,len(B)-1))
    print(rotation_k_while(A))          
            
            
            
