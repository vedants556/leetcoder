class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
 
        heap = []

        for row in matrix:
            heap += [-i for i in row]
            heapq.heapify(heap)
            while len(heap) > k:
                heapq.heappop(heap)
        return -min(heap)