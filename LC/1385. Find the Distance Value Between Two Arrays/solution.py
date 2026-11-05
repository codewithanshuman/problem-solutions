class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count = 0
        for a in arr1:
            if all(abs(a - b) > d for b in arr2):
                count += 1
        return count
