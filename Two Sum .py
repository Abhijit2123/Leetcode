class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, val in enumerate(nums):
            diff = target - val
            if diff in nums:
                y = nums.index(diff)
                ans = list((y,i))
        return ans