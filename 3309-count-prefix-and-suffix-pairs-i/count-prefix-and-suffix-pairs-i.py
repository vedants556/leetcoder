class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0

        for i in range(len(words)):
            for j in range(i + 1 , len(words)):

                w1,w2 = words[i], words[j]
                le = len(w1)
                if w1 == w2[:le] and w1 == w2[-le:]:
                    res += 1
        return res