import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = m+n-2
        b = m-1
        return math.factorial(a)//(math.factorial(b)*math.factorial(a-b))
            
