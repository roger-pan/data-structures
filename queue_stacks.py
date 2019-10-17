class Stack:
    def __init__(self):
        self._data = list()  # _ naming convention convention signals that you're not meant to access the data outside of the class

    def push(self, item):
        self._data.append(item)

    def pop(self):
        item = self._data[len(self._data) - 1]
        del self._data[len(self._data) - 1]  # Can also use self._data[-1]
        return item

    def peek(self):
        return self._data[len(self._data) - 1]

    def __len__(self):
        return len(self._data)

    def reverse(self):
        return self._data.reverse()


class Queue:

    def __init__(self):
        """
        Initialising the class
        """
        self.stack1 = Stack()
        self.stack2 = Stack()


    def enqueue(self, item):
        """
        Add item to end of queue
        """
        self.stack1.push(item)

    def dequeue(self):
        """
        Remove item from the queue.
        """
        length_ = len(self.stack1)
        while len(self.stack1) > 0:
            node1 = self.stack1.pop()
            self.stack2.push(node1)

        pop_result = self.stack2.pop()

        for j in range(length_ - 1):
            node2 = self.stack2.pop()
            self.stack1.push(node2)
        return pop_result


    def __len__(self):
        """
        Returns the length of the queue
        """
        return len(self.stack1)

    def reverse(self):
        return self.stack1.reverse()

