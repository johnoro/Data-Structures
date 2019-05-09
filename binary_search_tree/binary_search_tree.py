# each 'node' will be a B.S.T.
class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


  def insert_to(self, value, direction):
    if getattr(self, direction) is None:
      setattr(self, direction, BinarySearchTree(value))
    else:
      getattr(self, direction).insert(value)

  def insert(self, value):
    if value > self.value:
      self.insert_to(value, 'right')
    else:
      self.insert_to(value, 'left')


  def is_in(self, target, direction):
    node = getattr(self, direction)
    if node is None:
      return False
    if target == node.value:
      return True
    return node.contains(target)

  def contains(self, target):
    if target > self.value:
      return self.is_in(target, 'right')
    elif target == self.value:
      return True
    else:
      return self.is_in(target, 'left')


  def get_max(self):
    node = self
    while node.right is not None:
      node = node.right
    return node.value


  def for_each(self, cb):
    cb(self.value)
    if self.left is not None:
      self.left.for_each(cb)
    if self.right is not None:
      self.right.for_each(cb)
