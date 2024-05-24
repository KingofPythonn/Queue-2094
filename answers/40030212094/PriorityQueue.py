import time
import heapq

class PriorityQueue:
    def __init__(self):
        self._q = []

    def add(self, value, priority=0):
        return heapq.heappush(self._q, (priority, time.time(), value))

    def pop(self):
        return heapq.heappop(self._q)[-1]
    
    def isEmpty(self):
        return len(self._q) == 0
    
    def size(self):
        return len(self._q)
    
    
if __name__ == '__main__':
 pq = PriorityQueue()
 def f1(): print('hello')
 def f2(): print('hello00')
 def f3(): print(1)

 pq = PriorityQueue()
 pq.add(f1, priority=1)
 pq.add(f2, priority=2)
 pq.add(f3, priority=0)
 pq.pop()()
 

 print(pq.isEmpty())
 
print(pq.size())
