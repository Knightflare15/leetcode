class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = [-1]*len(heights)
        r = [len(heights)]*len(heights)
        stack = []
        maxi = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                l[i] = stack[-1]
            stack.append(i)
        stack.clear()
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                r[i] = stack[-1]
            stack.append(i)
        for i in range(len(heights)):
            maxi=max(maxi,heights[i]*(r[i]-l[i]-1))
        return maxi