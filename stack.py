class Stack:
    def __init__(self):
        self._data = list() # _ naming convention convention signals that you're not meant to access the data outside of the class
    
    def push(self, item):
        self._data.append(item)
            
    def pop(self): # O(1)
        if len(self._data) == 0:
            pass
        else:
            item = self._data[len(self._data) - 1]
            del self._data[len(self._data) - 1] # Can also use self._data[-1]
            return item
        
    def peek(self):
        if len(self._data) ==0:
            pass
        else:
            return self._data[len(self._data) - 1]
        
    def __len__(self):
        return len(self._data)

    def reverse(self):
        return self._data.reverse()

