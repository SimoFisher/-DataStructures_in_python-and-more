#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Doubly Linked List class
- append() -> method
- Check if the Doubly Linked List is Palindrome  -> Function plus computational cost
"""
### Algorithm to implement a function that checks if the file
### Doubly LinkedList Is palindrome

# INPUT: bidirectional linked queue with self.head.next and self.head.prev pointing to None with binary integer values ​​0 and 1
# OUTPUT: Returns True if queue is palindrome, otherwise returns False
      
 # Example:
  # 1->0->1->0->1->0->1 returns False
    # 1->0->1->0->1->0->1 returns True
      
    # the algorithmic idea consists in arriving first at the last node and only one cycle, then with a second while I compare the first node (previously saved in a variable) with the last, the second with the penultimate
     # and so on until they meet, the node where the pointers meet can be anything and the string remains a palindrome
     # limit cases: 1->0->1->0->0->1->0->1 if I take into account the two cases where the queue is both even and odd, the algorithm
     # it's no problem since in the case it's also then n/2+n/2 of complexity O(n/2)-> O(n/2) I'll have a comparison for all the data in the list
     # if DoublyLinkedList is odd I will have a comparison n/2 from left with n/2 from right -1 , so the complexity is:
         # T(n)=O(n/2+n/2 -1)=O(n/2-1)
           #T(n)=O(n) or the cost that I have to analyze all the values ​​of the LinkedList within the while

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
        
class DoublyLinkedList:
    def __init__(self):
           self.head=None
        
        
    def append(self,data):
        ''' append function, che appende un nodo con data alla fine della lista concatenata'''
        if self.head ==None:
            new_node=Node(data)
            new_node.prev=None
            self.head=new_node 
        else:
            new_node=Node(data)
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=new_node
            new_node.prev=cur
            # facciamo questo perchè il nuovo nodo creato viene accangiato con il puntatore prev. all'ultimo nodo della lista
            new_node.next=None
            # dopo aver aggiunto il nuovo nodo il puntatore punta a None,poichè siamo arrivati in fondo
            
            
    def coda_palindroma(self):
        '''funzione che restituisce True se la coda è palindroma, False altrimenti'''
        if self.head is None:return 'DLinkedList is empty'
        cur=self.head
        radice=cur
        while cur.next!=None:
            # ciclo while che mi restiruisce l'ultimo valore della DoublyLinkedList
            cur=cur.next
        while radice!=cur:
            # ciclo while fino a che sono diversi, quando sono sullo stesso nodo esce
            if radice.data==cur.data:
                print(radice.data,cur.data,':True')
                radice=radice.next 
                cur=cur.prev
                
            else:
                return False
            # ora ci siamo se i dati dei nodi sono diversi esce direttamente dalla funzione e ritorna False
        return True
    # attenzione richiamala dalla console sennò non ti stampa i return ..
          
    
    
    
if __name__=='__main__':
  dll=DoublyLinkedList()
 # 1->0->1->0->1->0->1
  dll.append(1)
  dll.append(0)
  dll.append(1)
  dll.append(0)
  dll.append(1)
  dll.append(1)
  dll.append(0)
  dll.append(1)
  dll.append(0)
  dll.append(1)
  dll.coda_palindroma()
# dll.print_list()
      