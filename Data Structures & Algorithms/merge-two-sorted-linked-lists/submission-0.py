# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #To avoid test cases, use a dummy node
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1 #This is how you insert current list value to dummy tail
                list1 = list1.next #this is how to update your pointer to next list value
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next #This is how to update tail pointer. Regardless of conditions
            
        #Conditions when one of them is longer than the other
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next




        
        
        