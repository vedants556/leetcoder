class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []  # list of queues
        num_to_group = {}  # nums[i] -> group's index
        
        # Create groups
        for n in sorted(nums):
            if not groups or abs(n - groups[-1][-1]) > limit:
                groups.append(deque())
            groups[-1].append(n)
            num_to_group[n] = len(groups) - 1
        
        # Build result by popping from groups
        return [groups[num_to_group[n]].popleft() for n in nums]
