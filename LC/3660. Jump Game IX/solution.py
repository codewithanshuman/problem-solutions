class Solution(object):
    def maxValue(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pref_max = [0] * n
        pref_max[0] = nums[0]
        for i in range(1, n):
            pref_max[i] = max(pref_max[i - 1], nums[i])
        

        ans = [0] * n
        ans[n - 1] = pref_max[n - 1]
        suf_min = nums[n - 1]

        for i in range(n - 2, -1, -1):
            if pref_max[i] > suf_min:
                ans[i] = ans[i + 1]
            
            else:

                ans[i] = pref_max[i]
            
            suf_min = min(suf_min, nums[i])
        return ans
