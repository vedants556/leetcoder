class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # Initialize the cache for the base cases
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        # Bottom-up DP approach to compute the minimum distance
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1])

        return cache[0][0]
