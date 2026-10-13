class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sq = sorted(x * x for x in nums)
        k = len(sq) // 2
        return sum(sq[k:]) - sum(sq[:k])
