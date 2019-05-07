class Heap:
  def __init__(self, comparator = lambda x, y: x > y):
    self.storage = []
    self.comparator = comparator
  
  def insert(self, value):
    index = len(self.storage)
    self.storage.append(value)
    self._bubble_up(index)

  def delete(self):
    topmost = self.get_priority()
    self.storage[0] = self.storage[-1]
    self.storage.pop()
    self._sift_down(0)
    return topmost

  def get_priority(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if index > 0:
      parent_index = self.parent(index)
      if self.compare(index, parent_index):
        self.swap(parent_index, index)
        self._bubble_up(parent_index)

  def _sift_down(self, index):
    left, right = self.left(index), self.right(index)
    if right < len(self.storage):
      max_child_index = left if self.compare(left, right) else right
    elif left < len(self.storage):
      max_child_index = left
    else:
      return
    if self.compare(max_child_index, index):
      self.swap(max_child_index, index)
      self._sift_down(max_child_index)

  def compare(self, i1, i2):
    return self.comparator(self.storage[i1], self.storage[i2])

  def swap(self, i1, i2):
    self.storage[i1], self.storage[i2] = self.storage[i2], self.storage[i1]

  def parent(self, index):
    return (index-1) // 2
  def left(self, index):
    return index*2 + 1
  def right(self, index):
    return index*2 + 2
