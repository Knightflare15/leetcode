class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if self.large and -self.small[0] > self.large[0]:
            small = heapq.heappop(self.small)
            small *= -1
            heapq.heappush(self.large, small)
            big = heapq.heappop(self.large)
            big *= -1
            heapq.heappush(self.small, big)

        while len(self.small) - len(self.large) > 1:
            short = heapq.heappop(self.small)
            short *= -1
            heapq.heappush(self.large, short)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2