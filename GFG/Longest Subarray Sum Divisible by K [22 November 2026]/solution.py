class Solution:
    def longestSubarrayDivK(self, arr, k):
        first = {0: -1}  
        prefix = 0
        best = 0
        for i, x in enumerate(arr):
            prefix = (prefix + x) % k
            if prefix in first:
                best = max(best, i - first[prefix])
            else:
                first[prefix] = i
        return best
