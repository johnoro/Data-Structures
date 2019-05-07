class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    index = len(self.storage)
    self.storage.append(value)
    self._bubble_up(index)
  
  # This logic was the hardest to get. I initially thought
  # this would work fine by just moving the second element up,
  # but it didn't play well with my
  # straightforward sift_down implementation.
  def delete(self):
    topmost = self.get_max()
    self.storage[0] = self.storage[-1]
    self.storage.pop()
    self._sift_down(0)
    return topmost

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    if index > 0:
      parent_index = self.parent(index)
      if self.storage[parent_index] < self.storage[index]:
        self.swap(parent_index, index)
        self._bubble_up(parent_index)

  def _sift_down(self, index):
    left, right = self.left(index), self.right(index)
    if right < len(self.storage):
      max_child_index = max(left, right,
        key=lambda i: self.storage[i])
    elif left < len(self.storage):
      max_child_index = left
    else:
      return
    if self.storage[max_child_index] > self.storage[index]:
      self.swap(max_child_index, index)
      self._sift_down(max_child_index)

  def swap(self, index1, index2):
    self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

  def parent(self, index):
    return (index-1) // 2
  def left(self, index):
    return index*2 + 1
  def right(self, index):
    return index*2 + 2
