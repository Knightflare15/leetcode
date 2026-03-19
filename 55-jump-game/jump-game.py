class Solution:
    def canJump(self, nums: List[int]) -> bool:
       arr = [False] * len(nums)
       arr[0] = True
       for i in range(len(nums)):
        if not arr[i]:
            continue
        for j in range(nums[i]):
            if i+j+1<len(nums):
                arr[i+j+1] = True
            if i+j+1 == len(nums)-1:
                return True
       print(arr)
       return arr[0] if len(arr) == 1 else False