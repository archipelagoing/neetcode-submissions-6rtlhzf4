# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1. find the middle using slow and fast pointers
# 2. reverse the 2nd half of hte list
# 3. Merge the 2 halves 1 by 1

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1. find the middle using slow & fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #2. reverse the 2nd half of the list 
        second = slow.next 
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        #3 Merge 2nd half 1 by 1
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


        