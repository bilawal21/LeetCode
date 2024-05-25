class Solution:
    def missingNumber(self,nums):

        n = len(nums)
        sum_all = (n * (n + 1) // 2)

        sum_given = sum(nums)

        missing_number = sum_all - sum_given

        return missing_number
    
obj = Solution()
    
given_array = [3,0,1]
result = obj.missingNumber(given_array)

print("The missing number is: ",result)
        