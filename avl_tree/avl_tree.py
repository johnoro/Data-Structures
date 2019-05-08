"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
  def __init__(self, node=None):
    self.node = node
    # init height to -1 because of 0-indexing
    self.height = -1
    self.balance = 0


  """
  Display the whole tree. Uses recursive def.
  """
  def display(self, level=0, pref=''):
    self.update_height()  # Update height before balancing
    self.update_balance()
    
    if self.node != None: 
      print ('-' * level * 2, pref, self.node.key, 
        f'[{self.height}:{self.balance}]', 
        'L' if self.height == 0 else ' ')
      if self.node.left != None: 
        self.node.left.display(level + 1, '<')
      if self.node.right != None:
        self.node.right.display(level + 1, '>')


  def h_cmp(self, direction, default = -1):
    node = getattr(self.node, direction)
    return node.height if node else default
  
  """
  Computes the maximum number of levels there are
  in the tree
  """
  def update_height(self):
    if self.node:
      if self.node.left:
        self.node.left.update_height()
      if self.node.right:
        self.node.right.update_height()
      self.height = max(self.h_cmp('left'), self.h_cmp('right')) + 1
    else:
      self.height = -1


  """
  Updates the balance factor on the AVLTree class
  """
  def update_balance(self):
    if self.node:
      if self.node.left:
        self.node.left.update_balance()
      if self.node.right:
        self.node.right.update_balance()
      self.balance = self.h_cmp('left', 0) - self.h_cmp('right', 0)
    else:
      self.balance = 0


  def rotate(self, from_dir, to_dir):
    node = self.node
    fro = getattr(node, from_dir)
    to = getattr(fro.node, to_dir)
    self.node = fro.node
    fro.node = to.node
    to.node = node

  """
  Perform a left rotation, making the right child of this
  node the parent and making the old parent the left child
  of the new parent. 
  """
  def left_rotate(self):
    self.rotate('right', 'left')

  """
  Perform a right rotation, making the left child of this
  node the parent and making the old parent the right child
  of the new parent. 
  """
  def right_rotate(self):
    self.rotate('left', 'right')


  def rotate_and_update(self, direction):
    getattr(self, f'{direction}_rotate')()
    self.update_height()
    self.update_balance()

  """
  Sets in motion the rebalancing logic to ensure the
  tree is balanced such that the balance factor is
  1 or -1
  """
  def rebalance(self):
    self.update_height()
    self.update_balance()
    while self.balance < -1 or self.balance > 1:
      if self.balance > 1:
        if self.node.left.balance < 0:
          self.node.left.rotate_and_update('left')
        self.rotate_and_update('right')
      if self.balance < -1:
        if self.node.right.balance > 0:
          self.node.right.rotate_and_update('right')
        self.rotate_and_update('left')
    

  """
  Uses the same insertion logic as a binary search tree
  after the value is inserted, we need to check to see
  if we need to rebalance
  """
  def insert(self, key):
    node = self.node
    if node is None:
      self.node = Node(key)
      self.node.left = AVLTree()
      self.node.right = AVLTree()
    elif key < node.key:
      self.node.left.insert(key)
    elif key > node.key:
      self.node.right.insert(key)
    else:
      raise ValueError(f'{key} already in tree.')
    self.rebalance()


tree = AVLTree()
tree.insert(5)
tree.insert(4)
tree.insert(6)
tree.insert(8)
tree.insert(3)
tree.insert(7)
tree.display()
