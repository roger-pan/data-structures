from linked_list import LinkedList, Node
class Dictionary:
    def __init__(self,length=1):
        """
        Initialises the dictionary
        """
        self._data = [None] * length
        self.length = length

    def get_index(self,key):
        """
        Returns the index of the key in the dictionary
        """
        hashed_value = abs(hash(key))
        index = hashed_value % self.length
        return index

    def set(self, key, value):
        """
        Sets a key and value pair in the dictionary
        """
        index = self.get_index(key) # Gets the index the key should be in

        if self._data[index] is None: # If there are no values in the index
            linked_list = LinkedList()  # Defining an empty LinkedList
            linked_list.insert_front(Node((key,value)))
            self._data[index] = linked_list
        else: # Defining what happens if there is already a linked list in the index
            self._data[index].insert_front((key,value))


    def get(self, key):
        """
        Gets the value for a key
        """
        index = self.get_index(key)  # Gets the index the key should be in
        value = self._data[index] # Value at the given index
        if value is None: #
            return None
        value = value.get_head() # If the value is not none then a linked list must exist. Get the head of the linked list
        while value is not None:
            if value.extract_value()[0] == key:
                return value.extract_value()[1]
            else:
                if value._next is not None:
                    value = value.next # Iterate onto the next node


    def contains(self, key):
        """
        True if dictionary contains key
        """
        if self.get(key) is None:
            return True
        else:
            return False

    def delete(self,key):
        """
        Deletes a key in a dictionary
        """
        index = self.get_index(key)
        value = self._data.extract_value().get(key)
        if value is None: # If value doesn't exist
            return
        else:
            self._data[index].delete((key,value))

x = Dictionary()
x.set(1,2)
print(x.get((1,2)))


