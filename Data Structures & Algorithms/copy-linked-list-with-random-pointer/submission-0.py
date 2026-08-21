"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None} #Create a hashmap for all copied nodes and make sure null current pointer returns null


        curr = head
        while curr:
            copy = Node(curr.val) #create a copy of the nodes and add the value
            oldToCopy[curr] = copy #set it to hashmap
            curr = curr.next #move our pointer
        
        #set copy.next and random pointers
        curr = head
        while curr:
            copy = oldToCopy[curr] #Give copy node of current
            copy.next = oldToCopy[curr.next] #Map the copy.next to the curr.next
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]

            
