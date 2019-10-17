import unittest

from queue import Queue

class TestQueue(unittest.TestCase):
    def test_enqueue_dequeue(self):

        # Arrange
        my_queue = Queue()
        my_queue.enqueue(1)
        my_queue.enqueue(2)

        # Act
        dequeue1 = my_queue.dequeue()
        dequeue2 = my_queue.dequeue()

        # Assert
        self.assertEqual(1,dequeue1, "First pop did not have expected value")
        self.assertEqual(2,dequeue2, "Second pop did not have expected value")





