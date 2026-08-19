# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
        
        #Find middle point with fast and slow pointers
        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        #How to split
        second_half = slow.next 
        prev = slow.next = None

        #Reverse the second half
        while second_half:
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp
        
        #Merge two halfs, second starts at last node which is previous node. First half starts at the head
        first_half, second_half = head, prev

        while second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half #reassign to second half
            second_half.next = temp1 #reassign to temp1 because we insert in between first and first.next
            #Now we shift our pointers
            first_half = temp1
            second_half = temp2
