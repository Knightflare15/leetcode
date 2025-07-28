class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        dp = [0] * (n + 1)
        dp[0] = startFuel

        for i in range(n):
            location, fuel = stations[i]
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    dp[t + 1] = max(dp[t + 1], dp[t] + fuel)

        for i in range(n + 1):
            if dp[i] >= target:
                return i

        return -1

