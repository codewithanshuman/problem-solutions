class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            parts = []
            for i in range(0, len(s), k):
                parts.append(str(sum(int(c) for c in s[i:i + k])))
            s = "".join(parts)
        return s
