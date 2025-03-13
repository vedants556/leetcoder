class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        pos = 0
        neg = 0
        for n in range(len(nums)):
            if nums[n] < 0:
                neg += 1
            if nums[n] > 0:
                pos += 1
            else:
                 continue
        return max(pos,neg)