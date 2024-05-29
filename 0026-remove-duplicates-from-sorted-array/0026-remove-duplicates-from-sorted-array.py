class Solution:
    def removeDuplicates(self, nums):
        l = 1

        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l
        

obj = Solution()
input_nums = [1,1,2]
result = obj.removeDuplicates(input_nums)
print(result, input_nums)
        