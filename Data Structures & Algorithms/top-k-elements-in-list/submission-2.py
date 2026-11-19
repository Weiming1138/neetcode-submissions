class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) #Count the number of times each number shows up 

        freq = [[] for i in range(len(nums) + 1)] #Create empty buckets

        for num, c in count.items(): #Take counted elements and organize into each of my freq buckets based on how many times they appear
            freq[c].append(num)

        res = []

        for i in range(len(freq) - 1, 0, -1): #Loop backwards from last index to first
            for n in freq[i]: #For each of the bucket of index i, if numbers are in the bucket, loop
                res.append(n) #add the most frequent numbers in res
                if len(res) == k: #Check to see if res meets length k
                    return res