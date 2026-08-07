class Solution:
    def search(self, nums: List[int], target: int, low=0, high=None) -> int:
        if high is None:
            high = len(nums) - 1

        if low > high:
            return -1

        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.search(nums, target, mid + 1, high)
        else:
            return self.search(nums, target, low, mid - 1)