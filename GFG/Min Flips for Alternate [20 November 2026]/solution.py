class Solution:
    def minFlips(self, s):
        n = len(s)

        diff = 0
        for i, ch in enumerate(s):
            if int(ch) != i % 2:
                diff += 1
        return min(diff, n - diff)
