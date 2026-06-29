# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        slow = dummy
        fast = head

        #1. create the gap. 
        for x in range(n):
            fast = fast.next
        
        #2. Move both till fast is at the end
        while fast:
            slow = slow.next
            fast = fast.next
        
        # 3. Remove that node
        slow.next = slow.next.next

        return dummy.next


"""
This is a multiline string workaround.
As long as it isn't assigned to a variable,
Python will evaluate it and discard it.

I think we're gonna have to try to do something similar. 
We're gonna have a pointer go to the end of the linked list
go back n-1 elements, 
and do point that element to element.next.next

Problem: we cant go backwards in a ll

Have a fast pointer go n steps ahead,
slow pointer goes 1 by 1. 
When there are no more nodes,
 the slow pointer will be sitting before the node i want to delete

"""
        