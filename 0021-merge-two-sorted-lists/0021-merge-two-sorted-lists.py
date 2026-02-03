# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        current=dummy

        while list1 and list2:  #runs when both nodes still have nodes if one finishes exits loop 
            if list1.val<list2.val:
                current.next=list1
                list1=list1.next
            else:
                current.next=list2
                list2=list2.next
            #despite you choose list1 or list2 you need to move current to next element so it stores the latest val
            current=current.next

        current.next=list1 or list2  # attach remaining nodes if on one gets over
        return dummy.next


        