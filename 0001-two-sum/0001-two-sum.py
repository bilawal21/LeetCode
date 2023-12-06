from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_dict = {}

        # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num

            # Check if the complement is already in the dictionary
            if complement in complement_dict:
                # If found, return the indices of the two numbers
                return [complement_dict[complement], i]

            # If not found, store the current number and its index in the dictionary
            complement_dict[num] = i

        # If no solution is found
        return None

# Example usage:
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)
