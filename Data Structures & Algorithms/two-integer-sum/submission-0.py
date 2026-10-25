class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, j in enumerate(nums):
            target_sum = target - nums[i]
            if target_sum in seen:
                return[seen[target_sum], i]
            else:
                seen[nums[i]] = i
