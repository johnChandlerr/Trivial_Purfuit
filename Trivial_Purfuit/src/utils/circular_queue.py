

class CircularQueue:
    """
    A queue in which dequeue() does not remove the item from the queue and
    once dequeue() gets to the end, it loops back to the front to return the
    first element in the queue.
    """

    def __init__(self, items=None):
        """
        Constructor
        :param items: The list of items to put in the queue if provided.
        """
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
        """
        Enter an item into he queue.
        :param item: The item to enter.
        :return: True if successful.
        """
        self.queue.append(item)
        self.tail = (self.tail + 1)
        return True

    def dequeue(self):
        """
        Get the next element from the queue, circling back to the front if at the end.
        :return: The next element from the queue.
        """
        if len(self.queue) == 0:
            return None

        item = self.queue[self.head]
        self.head = (self.head + 1) % len(self.queue)
        return item

    def size(self):
        """
        Get the size of the queue.
        :return: The queue's size.
        """
        return len(self.queue)