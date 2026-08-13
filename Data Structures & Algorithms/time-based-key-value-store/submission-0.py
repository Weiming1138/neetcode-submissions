class TimeMap:

    def __init__(self):
        self.hash = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key] = []
        self.hash[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.hash.get(key, [])
        l, r = 0, len(pairs) - 1 
        res = ""

        while l <= r:
            mid = (l + r) // 2
            timestamp_prev = pairs[mid][0]

            if timestamp_prev <= timestamp:
                l = mid + 1
                res = pairs[mid][1]
            else:
                r = mid - 1

        return res
