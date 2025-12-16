class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setter = set()
        for i in nums:
            setter.add(i)
        if len(nums) == len(setter):
            return False
        return True
