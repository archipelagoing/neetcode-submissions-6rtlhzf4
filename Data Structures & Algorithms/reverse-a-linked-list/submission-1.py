# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Attempt 1: Recursion
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         #a. if list empty, return none
#         if not head:
#             return None
        
#         newHead = head
#         #b. Recurzively call the function 
#         if head.next:
#             newHead = self.reverseList(head.next)
#             head.next.next = head
#         head.next = None

#         return newHead


# Attempt 2: Iteration
# time o(n)
# space o(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next #a. save next node
            curr.next = prev #b. reverse the pointer
            prev = curr     #c. move prev to curr
            curr = temp     #d. move curr to temp
        return prev
        