from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque()
        output = []
        for i in range(k):
                while q and nums[q[-1]]<=nums[i]:
                    q.pop()
                q.append(i)
        output = []
        output.append(nums[q[0]])
        for i in range(k,len(nums)):
            if i-k == q[0]:
                q.popleft()
            while q and nums[q[-1]]<=nums[i]:
                    q.pop()
            q.append(i)
            output.append(nums[q[0]])

        return output