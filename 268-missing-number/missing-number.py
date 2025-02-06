class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        xorr = n
        for i in range(n):
            xorr ^= i  # XOR the index
            xorr ^= nums[i]  # XOR the number at nums[i]
        return xorr
