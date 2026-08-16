# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        current = head
        while current is not None:
            arr.append(current.val)
            current = current.next

        arr.reverse()

        current = head
        for val in arr:
            current.val = val
            current = current.next
            
        return head
