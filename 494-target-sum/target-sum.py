class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def baktak(i, tot):
            if i == len(nums):
                return 1 if tot == target else 0
            if (i,tot) in dp:
                return dp[(i, tot)]
            
            dp[(i,tot)]  = (baktak(i + 1, tot + nums[i]) +
                            baktak(i+1, tot - nums[i]))
            return dp[(i,tot)]
        return baktak(0,0)