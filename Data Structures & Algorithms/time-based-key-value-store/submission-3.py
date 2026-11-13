class TimeMap:

    def __init__(self):
        self.hash = {} # key => string, value => a list of value and timestamp -> [[value, timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash: #check if key exists in the hashmap, set empty list if it doesn't
            self.hash[key] = []
        self.hash[key].append((timestamp, value)) #append the list of the timestamp and value
        

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.hash.get(key, []) #find a key in the hashmap and pair it, if not, return an empty list
        l, r = 0, len(pairs) - 1 
        res = ""

        while l <= r: #make sure to get the last value
            mid = (l + r) // 2
            timestamp_prev = pairs[mid][0] 

            if timestamp_prev <= timestamp: #check if the pair [value, timestamp] is less than or equal to timestamp we search for (can confirm its a valid value)
                res = pairs[mid][1] #value at index m
                l = mid + 1 #update left pointer to search right pointer
            else:
                r = mid - 1 #invalid value so we cant search result, because its supposed to be increasing order

        return res
