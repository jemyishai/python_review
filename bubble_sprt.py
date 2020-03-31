bubble sort -
n-1 coparison for the n-1 number of items in the array - the largest item "bubbles up" through each pass through
so (n-1) iterations times (n-1) comparisons means the efficiency is n squared - two n + 1
worst case and best average case is O(n squared); best case is O of n;
space complexity is O of 1
https://en.wikipedia.org/wiki/Bubble_sort

If you were to perform a bubble sort on the following array, what would the third iteration look like (ie after bubbling all the way up 3 times)?
[21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
after 1st pass: [4,1,3,9,20,21,6,21,14,25]
after 2nd pass: [1,3,4,9,20,6,21,14,21,25]
after 3rd pass: [1,3,4,9,6,20,14,21,21,25]

[21, 4, 1, 3, 9, 20, 25, 6, 21, 14] (Original Array)
[4, 1, 3, 9, 20, 21, 6, 21, 14, 25] (1)
[1, 3, 4, 9, 20, 6, 21, 14, 21, 25] (2)
[1, 3, 4, 9, 6, 20, 14, 21, 21, 25] (3)
[1, 3, 4, 6, 9, 14, 20, 21, 21, 25] (4)
