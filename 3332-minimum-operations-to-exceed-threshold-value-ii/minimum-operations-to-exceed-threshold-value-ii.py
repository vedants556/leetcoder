class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapq.heapify(nums)
        for x in range(len(nums) - 1):
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            if x < k:
                h = x * 2 + y 
                heapq.heappush(nums, h)
                count += 1
            else:
                return count
        return count


