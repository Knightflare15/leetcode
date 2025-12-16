class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setter = set()
        for i in nums:
            if i in setter:
                return True
            setter.add(i)
        return False
