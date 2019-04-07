
class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def append(self, new_element):
        """
        Adds an element to the end of the list.
        Saves a reference to it at the tail property, in case head already exists
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
            # save a reference to the last appended element in the tail property.
            self.tail = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        position_count = 1
        while current.next and position_count < position:
            if current.next:
                position_count += 1
                current = current.next
            else:
                return None
        
        return current
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        previous = self.get_position(position - 1)
        after_new = self.get_position(position)
        if after_new:
            new_element.next = after_new
            
        previous.next = new_element
        return
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if value == 1:
            self.head = self.head.next
            return
        if current.value == value:
            previous = self.get_position(current.value - 1)
            previous.next = current.next.next
            current.next = None
            return
        while current.next:
            current = current.next
            if current.value == value:
                previous = self.get_position(current.value - 1)
                previous.next = current.next.next
                current.next = None
                return
    
    def insert_first(self, new_element):
        # Insert element to the head of the list
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        first_element = None
        if self.head:
            if self.head.next:
                first_element = self.head
                # Remove the head, making the next element as the head
                self.head = self.head.next
                return first_element
            else:
                # In this case we only have the head to delete
                first_element = self.head
                self.head = None
                return first_element
        else:
            # We have no elements in the list, return None
            return first_element
