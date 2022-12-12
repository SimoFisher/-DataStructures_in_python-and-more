# -*- coding: utf-8 -*-

"""
Given a binary tree T, rooted and with n nodes, we define a node u of
T balanced if the left subtree of u and the right subtree of u have
both the same number of nodes.
Design an algorithm that, given the pointer r to the root of a tree
binary stored through records and pointers, returns in O(n) time the
number of its balanced nodes
"""


## INPUT: binary tree T with n-nodes, root r
## OUTPUT: the number of its balanced nodes

class TreeNode:
      def __init__(self,data=0,left=None,right=None):
          ''' first i need to create a constructor for the node 
          with pointers one to the left one to the right and another record with the value'''
          self.data=data 
          self.left=left
          self.right=right

def balanced_nodes_recursive(T)->int:
     '''  I follow a crossing logic in PostOrder, where I first evaluate the leaves 
     if there are any, cost Theta(n), summation of constant from 0 to n-1, T(n)=Theta(n)'''
     r=T
     if r is None: return (0,0)
     (nsx,eqsx)=balanced_nodes_recursive(r.left) # on return from recursive calls, save the information in a tuple-pair
     (ndx,eqdx)=balanced_nodes_recursive(r.right)
     eq=eqsx+eqdx
     if nsx==ndx: # if the number of nodes balenced ++, remember that also the leaves are balenced nodes no left.child no right.child
        eq+=1
        print(eq)  
     return (eq,nsx+ndx+1) 
    ## finally return the tupla-pair plus one , rememer the prime root





if __name__ == '__main__':
     TBS=TreeNode(10) ## root.principal
     TBS.left=TreeNode(7) # 7 correct 
     TBS.right=TreeNode(15)
     TBS.left.left= TreeNode(3)
     #tbs.right.right=TreeNode(20)
     TBS.left.right=TreeNode(9)
     print(balanced_nodes_recursive(TBS))
    



