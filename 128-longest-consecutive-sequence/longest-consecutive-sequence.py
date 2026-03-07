class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        k = 0

        for i in numset:
            if i-1 not in numset:
                curr = i
                tmp = 1

                while curr+1 in numset:
                    curr += 1
                    tmp += 1

                k = max(k, tmp)

        return k