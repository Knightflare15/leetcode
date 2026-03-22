class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) - 1
        while l<r:
            if numbers[r]+numbers[l] - target >0:
                r-=1
            elif numbers[r] + numbers[l] - target<0:
                l+=1
            else:
                return [l+1,r+1]
        return []
