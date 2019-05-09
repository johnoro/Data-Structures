Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?

Constant, `O(1)`.

2. What is the runtime complexity of `dequeue`?

Constant, `O(1)`.

3. What is the runtime complexity of `len`?

Constant, `O(1)`.

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

Linear based on the size of the BST, `O(k)`.

2. What is the runtime complexity of `contains`?

Linear based on the size of the BST, `O(k)`.

3. What is the runtime complexity of `get_max`? 

Linear based on the size of the BST, `O(k)`.

## Heap

1. What is the runtime complexity of `_bubble_up`?

Logarithmic based on the size of the heap, `O(log(k))`.

2. What is the runtime complexity of `_sift_down`?

Logarithmic based on the size of the heap, `O(log(k))`.

3. What is the runtime complexity of `insert`?

Logarithmic based on the size of the heap, `O(log(k))`.

4. What is the runtime complexity of `delete`?

Logarithmic based on the size of the heap, `O(log(k))`.

5. What is the runtime complexity of `get_max`?

Constant, `O(1)`.

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

Constant, `O(1)`.

2. What is the runtime complexity of `ListNode.insert_before`?

Constant, `O(1)`.

3. What is the runtime complexity of `ListNode.delete`?

Constant, `O(1)`.

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

Constant, `O(1)`.

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

Constant, `O(1)`.

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

Constant, `O(1)`.

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

Constant, `O(1)`.

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

Constant, `O(1)`.

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

Constant, `O(1)`.

10. What is the runtime complexity of `DoublyLinkedList.delete`?

Constant, `O(1)`.

11. (10.5) Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

Due to having to resize/recreate the array, JavaScript's array `splice` worst-case runtime complexity would be `O(n)`. This means that the doubly linked list's `delete` is better.
