from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the freq of each element
        freq_map = Counter(nums)

        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap,(freq,num))
            if len(heap)>k:
                heapq.heappop(heap)

        return [num for freq, num in heap]

         