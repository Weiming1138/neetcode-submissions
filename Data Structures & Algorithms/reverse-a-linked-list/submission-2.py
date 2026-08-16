# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #Iterative
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head #Initialize pointers

        while curr is not None: #Reverse pointers
            next = curr.next #keep track of node curr was pointing to
            curr.next = prev #change direction of pointer to the prev node
            prev = curr #move our pointers up
            curr = next

        return prev #prev keeps track of last node of original list which would have become our first node of new list