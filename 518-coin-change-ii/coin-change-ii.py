class Solution:
    def change(self, target: int, coins: List[int]) -> int:
        arr = [0]*(target+1)
        arr[0] = 1
        for i in coins:
            for j in range(i,target+1):
                arr[j] +=arr[j-i]
        return arr[target]
