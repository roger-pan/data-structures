import unittest

from stack import Stack

class TestStack(unittest.TestCase):

    def test_push_pop(self):
        
        # Arrange
        my_stack = Stack()
        my_stack.push(1)
        my_stack.push(2)
        
        # Act
        pop1 = my_stack.pop()
        pop2 = my_stack.pop()
        
        # Assert
        self.assertEqual(2, pop1, "first pop did not have the expected value")
        self.assertEqual(1, pop2, "second pop did not have the expected value")

    def test_push_pop_2(self):

        # Arrange
        my_stack = Stack()
        length_1 = len(my_stack)
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)

        # Act
        pop1 = my_stack.pop()
        pop2 = my_stack.pop()

        length_2 = len(my_stack)
        length_diff = length_2 - length_1

        # Assert
        self.assertEqual(3,pop1,"First pop did not have expected value")
        self.assertEqual(2,pop2, "Second pop did not have expected value")
        self.assertEqual(1,length_diff, "Length difference did not have expected value")
