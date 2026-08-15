class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2 #Partitions
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A): #Ensure A will be the minimum/smallest length
            A, B = B, A
        
        l, r = 0, len(A) - 1
        
        while True:
            midA = (l + r) // 2 #Middle point for A and B, then we check to see if left partition right most value (Aleft) is <= right partition left most value (Bright) and vice versa in order to confirm that we have a proper left partition
            midB = half - midA - 2 
            #float("-inf") and inf for cases where our Aleft/right and Bleft/right are the last values in the array and they dont go out of bounds!
            Aleft = A[midA] if midA >= 0 else float("-infinity")
            Aright = A[midA + 1] if (midA + 1) < len(A) else float("infinity")
            Bleft = B[midB] if midB >= 0 else float("-infinity")
            Bright = B[midB + 1] if (midB + 1) < len(B) else float("infinity")
            #If we do, we then need to check if the length of both A and B are even or odd, if odd, we return the minimum between Aright and Bright because when we combine the two together, their values would be next to each other, and one of them would have to be the median value
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
            #Otherwise, we can return the max value of our left partition and minimum of our right partition and divide it by 2 to find out median
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright: #if the left partitions are incorrect, corresponding to the right most value of the left partition, then we'd move our pointer l and r accordingly
                r = midA - 1
            else:
                l = midA + 1