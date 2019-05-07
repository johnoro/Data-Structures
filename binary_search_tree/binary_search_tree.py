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
    n = self.right
    if n is None:
      return self.value
    while n.right is not None:
      n = n.right
    return n.value

  def for_each(self, cb):
    pass
