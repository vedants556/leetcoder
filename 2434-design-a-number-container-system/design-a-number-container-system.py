class NumberContainers:

    def __init__(self):
        self.index_map = {}
        self.num_map = defaultdict(list)


    def change(self, index: int, number: int) -> None:
        # Update index to number mapping
        self.index_map[index] = number

        # Add index to the min heap for this number
        heapq.heappush(self.num_map[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_map:
            return -1

        # Keep checking top element until we find valid index
        while self.num_map[number]:
            index = self.num_map[number][0]

            # If index still maps to our target number, return it
            if self.index_map.get(index) == number:
                return index

            # Otherwise remove this stale index
            heapq.heappop(self.num_map[number])
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)