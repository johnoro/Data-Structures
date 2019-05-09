from dll import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # using DLL for constant time enqueue and dequeue
    self.dll = DoublyLinkedList()

  def __len__(self):
    return len(self.dll)

  def enqueue(self, item):
    self.dll.add_to_tail(item)
  
  def dequeue(self):
    return self.dll.remove_from_head()

  def len(self):
    return len(self)
