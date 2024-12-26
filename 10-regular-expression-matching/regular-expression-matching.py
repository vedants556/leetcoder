class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Top-Down Memoization approach
        cache = {}

        def dfs(i, j):
            # Check if the result for the pair (i, j) is already computed
            if (i, j) in cache:
                return cache[(i, j)]

            # If both strings are completely traversed, it's a match
            if i >= len(s) and j >= len(p):
                return True

            # If pattern is exhausted but string is not, it's a mismatch
            if j >= len(p):
                return False

            # Check if the current characters match or if the pattern has a '.'
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # If the next character in the pattern is '*', we have two cases:
            # 1. We skip the '*' and the preceding character (i.e., consider pattern[j+2])
            # 2. If there's a match, we can consume one character of string `s` and keep the `*` (i.e., dfs(i+1, j))
            if j + 1 < len(p) and p[j + 1] == "*":
                cache[(i, j)] = (dfs(i, j + 2) or (match and dfs(i + 1, j)))
                return cache[(i, j)]

            # If there's a match at this position, continue with the next character in both strings
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            # If no match, return False for this pair
            cache[(i, j)] = False
            return False

        # Start the DFS from the beginning of both the string and the pattern
        return dfs(0, 0)
