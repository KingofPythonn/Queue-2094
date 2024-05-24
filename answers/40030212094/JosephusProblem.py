from circularquque import CircularQueue


class jos:
 def josephus(n, k):
    queue = CircularQueue(n)

    for i in range(1, n + 1):
        queue.enqueue(i)

    while queue.size > 1:
        for _ in range(k - 1):
            queue.enqueue(queue.dequeue())
        queue.dequeue()

    return queue.dequeue()
