class Node:
    # Initialising the class
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.first_node = None
        self.last_node = None
        
    def insert_front(self,item):
        new_node = Node(data=item)
        new_node.next = self.first_node
        self.first_node.previous = new_node
        self.first_node = new_node

    def insert_back(self,item):
        new_node = Node(data=item)
        while node is not None:
            node = node.next_node

        new_node.previous = self.last_node
        self.last_node.next = new_node
        self.last_node = new_node

        
    def pop_front(self):
        front_node = self.first_node
        self.first_node = front_node.next
        return front_node.data
    
    def pop_back(self):
        last_node = self.last_node
        self.last_node = last_node.previous
        return last_node.data





