# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        second = dummy
        first = head

        for i in range(n): #Move the first pointer ahead n times
            if first is None:
                break
            first = first.next

        while first: #move the pointers
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next #DummyNode is anchor/before head value and returns the updated linked list with .next

        
        

        




            

        