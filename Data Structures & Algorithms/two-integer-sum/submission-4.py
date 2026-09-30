class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            find = target - value
            if find in seen.keys():
                return [seen[find], index]
            seen[value] = index