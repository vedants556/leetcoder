class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        curr_maz = -1
        res = 0

        for i , n in enumerate(arr):
            curr_maz = max(n , curr_maz)

            if curr_maz == i:
                res += 1
        return res