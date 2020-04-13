# Heaps:

# -Specific type of tree
# -Root value is either maximum or minimum value in the tree, max-heap or min-heap
#   In Max-heap, a parent must have greater value than its child
#   In Min-heap, a parent must have lesser value than its child

# -Not necesarily Binary, a parent can have many children
# -In Binary Heapversions, all levels must be filled out in order to be complete
#   -Binary heap must be complete - all levels are filled out
#   -Added from left to right - if the last level isn't filled out, values are added left-to-right

#   -Peek is the max value - searching for it it happens in constant time
#   -Search is linear becuase we have to search the entire tree
#     -Worst case O(n)
#     -Average O(n/2,), which is O(n)
#   -We can quit the search if the element is larger than the root in a max-heap

#   Insert:
#     Stick new element in next open slot, and then reorder the tree
#     Compare the new element with its parent and swap when the child is larger (in Max-Heap)
#     Worst Case is when (in Max Heap), it needs to be moved to the top. O(log(n))

#   Extract:
#     Deletion is a more general case of extract
#     Root is removed
#     Right most leaf is placed in roots spot and then compare to its children swap where necesary
#     Worst case is O(logn)

# Heap Implementation:
#   Represented as trees, but usually stored as arrays
#     -Since each node would need pointers to left child, right child, and parents, the array implementation saves us space memory
#   For a max heap, numbers need to be sorted in descending order
#   0th item is root, the next two items are its children, the next for items make-up the next level, added left to right, etc etc,
#     The last level need not be filled in, but it is filled in from left to right
