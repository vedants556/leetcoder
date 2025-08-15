class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distro(x):
            stores = 0 
            for w in quantities:
                stores += math.ceil(w/x)
            return stores <= n

        l,r = 1, max(quantities)
        res = 0
        while l <= r:
            x = (l + r) // 2
            if can_distro(x):
                res = x
                r = x - 1
            else:
                l = x + 1
        return res