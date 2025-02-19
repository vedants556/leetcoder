class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total_happy = 3*(2**(n-1))

        res = []
        choices = "abc"
        left , right = 1 , total_happy

        for i in range(n):
            curr = left
            part_size = (right - left + 1) // len(choices)

            for c in choices:
                if k in range(curr , curr + part_size):
                    res.append(c)
                    left = curr
                    right = curr + part_size - 1
                    choices = "abc".replace(c, "")
                    break
                curr += part_size

        return "".join(res)