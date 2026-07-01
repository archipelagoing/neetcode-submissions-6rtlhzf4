# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        return self.divide(lists, 0, len(lists)- 1)

    def divide(self, lists, l, r):
            if l > r:
                return None
            if l == r:
                return lists[l]

            mid = l + (r-l) //2
            left = self.divide(lists, l, mid)
            right = self.divide(lists, mid+1, r)

            return self.conquer(left, right)

            mid = l + (r-l) //2

    def conquer(self,l1, l2):
            dummy = ListNode(0)
            curr = dummy # we build a temporary list to order everything in

            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1 
                    l1 = l1.next
                else:
                    curr.next = l2 
                    l2 = l2.next
                curr = curr.next
            
            if l1:
                curr.next = l1 
            else: 
                curr.next = l2 
            
            return dummy.next 


"""
ok how can we go about this
we have k sorted linked list, sorted in ascending order, we have to merge them all together in order
Brute force:
 - store all n nodes in an array, sort the array, and then convert the array into a linked list, 
 0(nlogn)

 How can we use the idea of merging 2 sorted linked lists?

"""