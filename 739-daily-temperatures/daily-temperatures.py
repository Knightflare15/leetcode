class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*(len(temperatures))
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                temp = stack.pop()
                output[temp] = i-temp
            stack.append(i)
        return output
            