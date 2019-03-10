from DataStructures.Queue import Queue

# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(q.peek())

# Test dequeue
# Should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print(q.dequeue()) 
# Should be 3
print(q.dequeue())
# Should be 4
print(q.dequeue())
q.enqueue(5)
# Should be 5
print(q.peek())