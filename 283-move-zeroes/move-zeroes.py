class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0  # pointer to place the next non-zero number

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
