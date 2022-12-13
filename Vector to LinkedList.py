#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## function that takes two arguments a pointer of type reference that initially points to null and an array .
### I build a LinkedList using the values ​​from the array
    
    
class Nodo:
    def __init__(self, key=None, next=None,head=None):
          self.key = key
          self.next = next
          self.head=head
          
          
          
          
def Create(p,A):
# generate a linked list using the elements of as keys
# an array, which terminates by returning the head of the created list
   p = None
   count=0
   for i in range(len(A),0,-1):
        P = Nodo(A[i-1],p)
        cur=P
        New_key(cur) 
        print(cur.key)
        count+=1 # Counting the nodes
   return 'number of nodes :' + str(count)


def New_key(cur):
    
    tmp=cur.key
  
    
   

if __name__=='__main__':
    A=[23,455,6,56,56,78,34]
    ll=Nodo()
    print(Create(ll,A))
      
