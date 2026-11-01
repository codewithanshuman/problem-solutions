class Solution:

    def maximumSubarray(self, arr: list[int]) -> int:
        no = float('-inf')  
        sq = float('-inf')  
        ans = float('-inf')

        for x in arr:
            prev_no = max(no, 0)
            new_sq = max(prev_no + x * x, sq + x)
            new_no = prev_no + x
            no, sq = new_no, new_sq
            ans = max(ans, no, sq)

        return ans
