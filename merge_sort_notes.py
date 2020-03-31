#Merge Sort
Made up of divide and conquer

divide into smaller arrays of two and one slots
build back up and start making comparisons - each array will require comparisons - an array of 3 will require 2 comparisons, and an array of 4 will require 3 comparisons; so if array is length m (of all the 'divide an conquer arrays'), than total comparions equal all the m-1 comparisons added up

n comparisons for log n steps ; so the efficiency  is O(nlogn)

auxilary space O(n) - assumes all the new arrays created are deleted after creation

comic inspired by merge Sort
https://xkcd.com/1185/

text book is in java but this may be helpful - https://algs4.cs.princeton.edu/22mergesort/
For merge sort, it's particularly worth reading up on top-down and bottom-up merge sort.

If you were to perform a merge sort on the following array, which is a possibility for what the second iteration might look like (ie after bubbling all the way 2 times)?
[21,4,1,3,9,20,25]
[21][4,1][3,9][20,25]
[21][1,4][3,9][20,25]
[1,4,21][3,9,20,25]
[]

** This quesiton is a bit poor because the language makes more sense for bubble sort - it's unclear what second iteration means. Here it means after two comparison operations within the presented merge-sort algorithm.

Depending on the way you design your merge sort, you could get a few different solutions, but this was the answer:

[21, 4, 1, 3, 9, 20, 25] (Original Array)
[21, 1, 4, 3, 9, 20, 25] (1)
[1, 4, 21, 3, 9, 20, 25] (2)
[1, 3, 4, 9, 20, 21, 25] (3)
