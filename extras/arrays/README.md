# Arrays

An array is a sequence of uniformly-typed elements stored in a contiguous block of memory.

How do you declare an array?

1. Determine how big the array needs to be
2. Request a block of memory that will fit the array
3. Receive the memory address of the reserved block
4. Write your values into the array

Example:

Create an array that stores the integers: 2, 3, 4, 5

1. Determine how big the array needs to be
  * An integer is 4-bytes so to store 4 integers, the array needs 16-bytes of space
2. Request 16-bytes of memory from the computer
3. Receive an address to your 16-bytes of reserved memory
4. Write the values of 2, 3, 4 and 5 into the array

```c
// I imagine this one would be something like this:
typedef struct Array {
  int cap;
  int len;
  int *nums;
} Array;

Array *array(int cap) {
  Array *arr = malloc(sizeof(Array));
  arr->cap = cap;
  arr->len = 0;
  arr->nums = malloc(sizeof(int) * cap);
  return arr;
}

void push(Array *arr, int num) {
  if (arr->len < arr->cap) {
    arr->nums[arr->len++] = num;
  }
}

int main(void) {
  Array *arr = array(4);
  for (int n = 2; n <= 5; n++) {
    push(arr, n);
  }
  
  int i = 0;
  while (i < arr->len - 1) {
    printf("%d, ", arr->nums[i++]);
  }
  printf("%d", arr->nums[i]);

  return 0;
}
```

A byte consists of 8-bits and a bit is either a 1 or a 0 so the resulting memory would look something like this:

25600    25601    25602    25603
00000000 00000000 00000000 00000010

25604    25605    25606    25607
00000000 00000000 00000000 00000011

25608    25609    25610    25611
00000000 00000000 00000000 00000100

25612    25613    25614    25615
00000000 00000000 00000000 00000101
