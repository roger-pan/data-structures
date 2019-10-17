import unittest
from doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def test_insert_front_pop_front(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.insert_front(1)
        doubly_linked_list.insert_front(2)

        pop_front = doubly_linked_list.pop_front()

        self.assertEqual(2,pop_front,"pop_front did not receive the right value")

    def test_insert_back_pop_back(self):
        doubly_linked_list = DoublyLinkedList()
        doubly_linked_list.insert_back(1)
        doubly_linked_list.insert_back(2)

        pop_back = doubly_linked_list.pop_back()

        self.assertEqual(2,pop_back, "pop_back did not receive the right value ")
