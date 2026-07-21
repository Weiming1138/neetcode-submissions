class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left != right:
            sum = numbers[left] + numbers[right]

            if sum == target:
                toReturn = [left + 1, right + 1]
                break
            elif sum > target:
                right -= 1
            else:
                left += 1

        return toReturn