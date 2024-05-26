class Solution:
    def twoSum(self, nums, target):
        prevMap = {} # val : index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
        

obj = Solution()
input_nums = [2,7,11,15]
target = 9
result = obj.twoSum(input_nums, target)
print(result)