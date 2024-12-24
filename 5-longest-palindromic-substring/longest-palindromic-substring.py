class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""  # The longest palindrome found
        resLen = 0  # Length of the longest palindrome

        # Iterate through each character in the string
        for i in range(len(s)):
            # Case 1: Odd length palindrome (centered at `i`)
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left:right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1

            # Case 2: Even length palindrome (centered between `i` and `i + 1`)
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left:right + 1]
                    resLen = right - left + 1
                left -= 1
                right += 1

        return res
