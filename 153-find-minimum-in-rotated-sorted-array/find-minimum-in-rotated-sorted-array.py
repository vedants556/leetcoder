class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] <= nums[r]:  # Left side is sorted
                res = min(res, nums[l])  # The minimum element could be at l
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:  # If m is greater than or equal to left, the min is in the right half
                l = m + 1
            else:
                r = m - 1

        return res
