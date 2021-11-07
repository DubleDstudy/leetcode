from heapq import heappush, heappop
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        h = []
        for key,value in Counter(tasks).items():
            heappush(h, (-1*value, key))
        while h:
            i, temp = 0, []
            while i <= n:
                time += 1
                if h:
                    x,y = heappop(h)
                    if x != -1:
                        temp.append((x+1,y))
                if not h and not temp:
                    break
                else:
                    i += 1
            for item in temp:
                heappush(h, item)
        return time