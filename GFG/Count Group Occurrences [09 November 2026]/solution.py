class Solution:
    def getCount(self, s, k):
        groups = [0] * 26

        for i, ch in enumerate(s):
            if i == 0 or ch != s[i - 1]:
                groups[ord(ch) - ord('a')] += 1

        return sum(1 for g in groups if g == k)
