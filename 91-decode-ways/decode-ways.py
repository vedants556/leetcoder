class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}  # Base case: 1 way to decode an empty string

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":  # If the current character is '0', no valid encoding
                return 0

            # Decode by considering the single character at index i
            res = dfs(i + 1)

            # Decode by considering the two-character number formed by s[i] and s[i+1]
            if (i + 1 < len(s) and 
                (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456"))):
                res += dfs(i + 2)

            # Store the result in dp for future reference
            dp[i] = res
            return res

        # Start DFS from the first character
        return dfs(0)
