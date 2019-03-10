class Queue:
    def __init__(self, head=None):
        self.storage = [head]
    
    def enqueue(self, new_element):
        """
        Adds an item to the end of the list
        """
        self.storage.append(new_element)

    def peek(self):
        """
        Returns the last item on the list without removing it
        """
        first_item = None
        if len(self.storage) >= 0:
            first_item = self.storage[0]
        
        return first_item
    
    def dequeue(self):
        """
        Removes the last item of the list and return it
        """
        if len(self.storage) >= 0:
            return self.storage.pop(0)
        else: 
            return None
        return self.storage.pop()