class Solution(object):
    def maxArea(self, height):
        sumo = 0
        l = 0
        r = len(height)-1
        while l<r:
            sumo = max(sumo,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            elif height[r]<height[l]:
                r-=1
            else:
                l+=1
                r-=1
        return sumo
            

                
        
        