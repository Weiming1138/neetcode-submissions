# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        first = second = head
        count = 0

        while first and count < n:
            first = first.next
            count += 1
        
        while first and first.next:
            second = second.next
            first = first.next

        if second is head and not first:
            head = head.next
        else:
            second.next = second.next.next
        
        return head
            