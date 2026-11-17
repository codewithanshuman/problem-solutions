class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        even, odd = 1, 0
        parity = 0
        result = 0
        for x in arr:
            parity ^= (x & 1)
            if parity:
                result += even
                odd += 1
            else:
                result += odd
                even += 1
        return result % MOD
