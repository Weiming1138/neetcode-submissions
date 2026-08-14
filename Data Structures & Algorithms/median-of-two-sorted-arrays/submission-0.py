class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_nums = sorted(nums1 + nums2)
        l, r = 0, len(sorted_nums) - 1

        for i in range(len(sorted_nums)):
            mid = (l + r) // 2

            if len(sorted_nums) % 2 == 0:
                return (sorted_nums[mid] + sorted_nums[mid + 1]) / 2
            else:
                return sorted_nums[mid]