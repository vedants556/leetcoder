class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right = sum(nums) #linear time
        left = 0
        res = 0

        for i in range(len(nums) -1 ):
            left += nums[i]
            right -= nums[i]

            res += 1 if left >= right else 0
        return res