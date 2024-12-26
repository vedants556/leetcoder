class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add 1 at both ends of the array to handle boundary cases
        nums = [1] + nums + [1]
        dp = {}

        # Define the dfs function to compute the maximum coins we can collect
        def dfs(left, right):
            if left > right:
                return 0  # Base case: no more balloons to burst
            if (left, right) in dp:
                return dp[(left, right)]  # Return already computed value

            dp[(left, right)] = 0
            for i in range(left, right + 1):
                # Calculate the coins we get by bursting the balloon at index i
                coins = nums[left - 1] * nums[i] * nums[right + 1]
                # Add the coins from bursting balloons to the left and right of i
                coins += dfs(left, i - 1) + dfs(i + 1, right)
                # Take the maximum result
                dp[(left, right)] = max(dp[(left, right)], coins)

            return dp[(left, right)]

        # Call dfs to calculate the maximum coins for the entire range
        return dfs(1, len(nums) - 2)
