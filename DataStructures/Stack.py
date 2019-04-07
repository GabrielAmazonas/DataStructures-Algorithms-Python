from .LinkedList import LinkedList
from .Element import Element

class Stack:
    def __init__(self, top=None):
        self.linkedList = LinkedList(top)

    def push(self, new_element):
        # Adding an element to the top of the stack, in this case, the last element
        self.linkedList.insert_first(new_element)
    
    def pop(self):
        return self.linkedList.delete_first()