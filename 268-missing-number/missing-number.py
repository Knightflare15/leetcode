class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(-1)
        i=0
        while i < n:
            while 0 <= nums[i] < n and nums[i] != nums[nums[i]]:
                correct = nums[i]
                nums[i], nums[correct] = nums[correct], nums[i]
            i += 1
        for i in range(n):
            if i != nums[i]:
                return i
        return n
        