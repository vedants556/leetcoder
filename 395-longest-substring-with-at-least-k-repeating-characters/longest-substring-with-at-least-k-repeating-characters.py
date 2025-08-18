class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(c))
        return len(s)
