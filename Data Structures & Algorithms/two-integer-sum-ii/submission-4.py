class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        output = []

        while left<=right:
            target_sum = numbers[left]+numbers[right]
            if target_sum < target:
                left += 1
            elif target_sum > target:
                right -= 1
            else: # =
                output.append(left+1)
                output.append(right+1)
                left += 1
                right -= 1

                return output

