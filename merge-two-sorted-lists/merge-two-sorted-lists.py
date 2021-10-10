# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(None)
        small = temp
        while l1 and l2:
            if l1.val < l2.val:
                small.next = l1
                l1 = l1.next
            else:
                small.next = l2
                l2 = l2.next
            small = small.next
            
        small.next = l1 or l2
        return temp.next