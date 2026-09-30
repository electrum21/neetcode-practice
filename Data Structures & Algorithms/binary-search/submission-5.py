class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums, 0, len(nums)-1, target)
        
    def helper(self, nums, low, high, target):
        midindex = (low+high)//2
        if high < low:
            return -1
        if target == nums[midindex]:
            return midindex
        elif target < nums[midindex]:
            return self.helper(nums, low, midindex-1, target)
        else:
            return self.helper(nums, midindex+1, high, target)
        