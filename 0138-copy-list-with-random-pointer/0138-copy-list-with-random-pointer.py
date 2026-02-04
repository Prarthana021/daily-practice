"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyMap={None:None}
        #map; key(purano node):value(naya node)
        curr=head
        while curr:
            copy = Node(curr.val)
            copyMap[curr]=copy
            curr=curr.next
        
        curr=head   #dont forget to reset curr
        while curr: #at any iteration copy represents one node 
        #copy creates node one by one at the end of the loop copy = last value of the node 
            copy=copyMap[curr]
            copy.next=copyMap[curr.next]
            copy.random=copyMap[curr.random]
            curr=curr.next
        return copyMap[head]    #it returns original copied node's head 

            




        