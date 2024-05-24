class CircularQueue:
    def __init__(self, string):
        self.queue = [None] * len(string)
        self.head = 0
        self.tail = 0
        self.size = 0
        for char in string:
            self.enqueue(char)

    def enqueue(self, item):
        if self.size == len(self.queue):
            raise ValueError("Circular queue is full")
        if self.is_empty():
            self.queue[self.tail] = item
        else:
            if self.tail == len(self.queue) - 1:
                self.tail = 0
            else:
                self.tail += 1
            self.queue[self.tail] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Circular queue is empty")
        max_ascii = ord(self.queue[self.head])
        max_index = self.head
        for i in range(self.size):
            index = (self.head + i) % len(self.queue)
            if ord(self.queue[index]) > max_ascii:
                max_ascii = ord(self.queue[index])
                max_index = indexresult = []
        current = self.head
        for i in range(self.size):
            if current == max_index:
                current = (current + 1) % len(self.queue)
                continue
            result.append(self.queue[current])
            current = (current + 1) % len(self.queue)
        self.queue[max_index] = None
        self.head = max_index
        self.size -= 1
        return "".join(result)

    def __str__(self):
        result = []
        current = self.head
        for i in range(self.size):
            if self.queue[current] is None:
                current = (current + 1) % len(self.queue)
                continue
            result.append(self.queue[current])
            current = (current + 1) % len(self.queue)
        return "".join(result)

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

# Example usage
cq = CircularQueue("abcd")
print(cq)
cq.dequeue()
print(cq)
cq.dequeue()
print(cq)
cq.enqueue("e")
cq.enqueue("f")
print(cq)