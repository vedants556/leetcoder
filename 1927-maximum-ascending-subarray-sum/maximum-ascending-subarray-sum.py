class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sum = nums[0]
        res = sum 
        
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                sum += nums[i]
            else :
                sum = nums[i]
            res = max(res, sum)


        return res
