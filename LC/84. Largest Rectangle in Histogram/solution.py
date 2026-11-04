class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        best = 0
        n = len(heights)
        for j in range(n + 1):
            h = heights[j] if j < n else 0
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = j - left - 1
                area = height * width
                if area > best:
                    best = area
            stack.append(j)
        return best
