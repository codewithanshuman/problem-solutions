class Solution:
    def subarrayXor(self, arr):
        n = len(arr)
        if n % 2 == 0:
            return 0
        res = 0
        for i in range(0, n, 2):
            res ^= arr[i]
        return res
