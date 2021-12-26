class MedianFinder(object):

    def __init__(self):
        self.med, self.odd, self.heaps = 0, 0, [[], []]

    def addNum(self, x):
        big, small = self.heaps
        if self.odd:
            heapq.heappush(big, max(x, self.med))
            heapq.heappush(small, -min(x, self.med))
            self.med = (big[0] - small[0]) / 2.0
        else:
            if x > self.med:
                self.med = heapq.heappushpop(big, x)
            else:
                self.med = -heapq.heappushpop(small, -x)
        self.odd ^= 1

    def findMedian(self):
        return self.med