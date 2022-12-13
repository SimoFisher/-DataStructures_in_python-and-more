#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:16:14 2022

@author: landau
"""

## Write a function that validates a binary search tree, which has 
### the property of having the parent between left and right children, with keys all distinct from each other.


class Node:
  def __init__(self, value, left=None, right=None,root=None):
    """
      Create a node (vertex) of the tree
      Parameters
      ----------
      value : int
        Represent the value stored in the node
      left_node : Node
        Represent the left child of the node
      right_node : Node
        Represent the right child of the node
    """
    self.value = value
    self.left = left
    self.right = right
    


    

def start_verificaBTS(nodo):
    lista=[]
    verificaBST(nodo,lista)
    for i in range(1,len(lista)):
        if lista[i] <= lista[i-1]: return False
        # when I return from the recursive calls I compare the two children respectively on the left and on the right, 
        # if it turns out that the one on the right is smaller then I exit the loop and return False,
        #   otherwise when I get to the end I return True
    return True
    
    
def verificaBST(nodo,lista):
    if nodo is None: return  
    verificaBST(nodo.left,lista)
    lista.append(nodo.value)
    ## In Order calling first nodo.left , after nodo.root, finally nodo.right
    verificaBST(nodo.right,lista)

    
    

        
    
    
    
if __name__=='__main__':
    root=Node(10) ## Master root
    root.left=Node(7)
    root.right=Node(17)
    root.left.left= Node(6)
    root.right.right=Node(25)
    root.left.right=Node(9)
    root.right.left=Node(15)
    root.left.left=Node(5)
    print(start_verificaBTS(root))
       
    
    
    
    