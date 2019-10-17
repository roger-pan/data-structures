class Node:
    """
    A node is a single datapoint in a linked list
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def value(self):
        self.value = self.data

class LinkedList:
    def __init__(self):
        """
        Creates a new linked list
        """
        self.head= None

    def get_head(self):
        """
        Returns the first value of a linked list
        :return:
        """
        return self.head

    def insert_front(self, item):
        """
        Insert an item at the front of the list
        """
        new_node = Node(data=item) # New node to be inserted
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head # Assigning the pointer for the new node to be the first node
            self.head = new_node # Assigning the first node as the new node

        
    def pop_front(self):
        """
        Remove an item from the front
        """
        current = self.head # Defining a variable to store the first node
        if current is None:
            return None
        elif current.next is None: # If length is 1
            self.head = None
            return current
        elif current.next.next is not None: # If the length is at least 2
            current.next = current.next.next
            self.head = current.next # Changing the first node to the second note
            return current.data # Returning the popped node



    def delete(self, key):
        """
        Deletes all instances of key in the linked list
        :param key:
        :return:
        """
        current = self.head

        # If the list has no values then return
        if current == None:
            return

        # If the head is the key then set the head as the next value
        if current is not None and current.data == key:
            self.head = current.next
            current = None
            return

        while current is not None:
            previous = current # Storing current node in variable previous
            current = current.next # Current node is the next node
            if current.data == key:
                previous.next = current.next # pointer for previous node is equal to the next node after current
                current = None # delete the current Node

    def reverse(self):
        """
        Reverses the order of the linked list
        :return:
        """
        previous = None # defining a variable for previous node starting with None
        current = self.head # current node starts at the head

        if current is None or current.next is None:
            return
        while current is not None:
                current.next = previous # Assigning the pointer for the current node to the previous value
                previous = current  # Assigning the current value to the variable previous
                if current.next is not None:
                    current = current.next # Iterating to the next node
                else:
                    break
        self.head = previous # Asigning the first value as the last
        self.head.next = None

    def __len__(self):
        """
        Returns the length of the list
        """
        counter = 0
        node = self.head

        while node is not None:
           node = node.next
           counter +=1
        return counter

    # def __iter__(self):
    #     current = self.head
    #     while current.next is not None:
    #         yield current
    #         current = current.next


























