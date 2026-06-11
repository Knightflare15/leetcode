class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        l_max = l
        r_max = r
        sumo = 0
        while l<=r:
            if height[l]>height[l_max]:
                    l_max=l
            if height[r]>height[r_max]:
                    r_max=r
            if height[l]<height[r_max]:
                sumo+=min(height[r_max],height[l_max])-height[l]
                l+=1
            elif height[r]<height[l_max]:
                sumo+=min(height[r_max],height[l_max])-height[r]
                r-=1
            else:
                r-=1
                l+=1
        return sumo
