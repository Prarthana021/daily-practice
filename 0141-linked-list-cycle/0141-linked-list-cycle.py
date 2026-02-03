# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=fast=head

        while fast and fast.next: #fast lai 2 steps le move so make sure move garna lai they exist 
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                return True
        return False
            

        