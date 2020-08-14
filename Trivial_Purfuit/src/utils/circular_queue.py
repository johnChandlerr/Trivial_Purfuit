

class CircularQueue:

    def __init__(self, items=None):
        if items is None:
            items = list()
        self.queue = items
        self.head = 0
        if len(self.queue) == 0:
            self.tail = 0
        else:
            self.tail = (len(items) - 1)
        self.next_index = 0

    def enqueue(self, item):
        self.queue.append(item)
        self.tail = (self.tail + 1)
        return True

    def dequeue(self):
        if len(self.queue) == 0:
            return None

        item = self.queue[self.head]
        self.head = (self.head + 1) % len(self.queue)
        return item

    def size(self):
        return len(self.queue)