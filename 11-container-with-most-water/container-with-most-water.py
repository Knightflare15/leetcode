class Solution(object):
    def maxArea(self, height):
           l = 0
           r = len(height)-1
           sumo = 0
           while l<r:
                sumo = max(sumo,min(height[l],height[r])*abs(l-r))
                if height[r]>height[l]:
                    l+=1
                elif height[l]>height[r]:
                    r-=1
                else:
                    r-=1
                    l+=1
           return sumo
            

                
        
        