class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def __len__(self):
    return len(self.storage)

  def enqueue(self, item):
    self.storage.append(item)
  
  def dequeue(self):
    try:
      return self.storage.pop(0)
    except IndexError:
      return None

  def len(self):
    return len(self)
