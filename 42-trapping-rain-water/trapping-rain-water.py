class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        leftmax = [0]*l
        rightmax = [0]*l
        
        leftmax[0] = height[0]
        rightmax[l-1] = height[l-1]
        maxi = leftmax[0]
        for i in range(1,l):
            maxi = max(maxi,height[i])
            leftmax[i] = maxi
        maxi = rightmax[l-1]
        for i in range(l-2,-1,-1):
            maxi = max(maxi,height[i])
            rightmax[i] = maxi
        final = 0
        print(leftmax)
        print(rightmax)
        for i in range(1,l-1):
            final+=min(leftmax[i],rightmax[i])-height[i]
        return final    
