import unittest
from linked_list import LinkedList

class test_linked_list(unittest.TestCase):

    def test_insert_front_pop_front(self):
        # Arrange
        linked_list = LinkedList()
        linked_list.insert_front(1)
        linked_list.insert_front(2)

        # Act
        pop1 = linked_list.pop_front()

        # Assert
        self.assertEqual(2, pop1, "first pop did not have the expected value")

    def test_delete_pop(self):
        linked_list = LinkedList()
        linked_list.insert_front(1)
        linked_list.insert_front(2)
        linked_list.delete(1)

        pop2 = linked_list.pop_front()

        self.assertEqual(2, pop2, "delete did not have expected value")

    def test_reverse_pop(self):
        linked_list = LinkedList()
        linked_list.insert_front(1)
        linked_list.insert_front(2)
        linked_list.insert_front(3)
        reverse_list = linked_list.reverse()

        pop3 = reverse_list.pop_front()

        self.assertEqual(1, pop3, "reverse list did not have expected value")












