class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #initialize pointers, output, and queue
        output = []
        l = r = 0
        q = collections.deque()

        while r < len(nums):
            #while our q is not empty and rightmost value of our q is less than the value we are adding
            while q and nums[q[-1]] < nums[r]: #remove smaller values from the q
                q.pop()
            q.append(r) #add index of r into q

            #if left values out of bounds/out of window
            if l > q[0]:
                q.popleft()

            #make sure window is actually size k
            if (r + 1) >= k: 
                output.append(nums[q[0]]) #append max value, which is leftmost position
                l += 1 #only increment when our window is size k
            r += 1
        
        return output
            
            