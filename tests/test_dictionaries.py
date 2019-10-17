import unittest
from dictionary import Dictionary

class TestDictionary(unittest.TestCase):

    def test_set_get_index(self):
        d = Dictionary()
        d.set(key=1,value=2)
        value1 = d.get(1)
        value2 = d.get(1)
        self.assertEqual(0,value1-value2, "get_index values are not equal ")

    def test_set_get(self):
        dictionary = Dictionary()
        dictionary.set(key=1, value=2)
        value1 = dictionary.get(1)

        self.assertEqual(2,value1,"set_get value 1 did not have the right value")

    def test_set_contains(self):
        dictionary = Dictionary().set(key=1, value=2)
        value = dictionary.contains(1)

        self.assertEqual(True,value,"set_contains did not have the right value")

    def test_delete_get(self):
        dictionary = Dictionary().set(key=1, value=2)
        dictionary.delete(key=1)
        value = dictionary.get(key=1)

        self.assertEqual(None,value,"delete_get did not have the right value")







