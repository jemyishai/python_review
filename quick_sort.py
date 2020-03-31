#Quick Sort Notes
PIVOT - sort values around it (larger & smaller), recurse &then pick more pivots and cotinue sorting
-convention is to pick last element as pivot

-IN PLACE SORT --
worst case scenario is if the pivot is in place becasue then we need to make all the comparisons
O(n squared)
best is n log n
average is also n log

if an array is sorted or nearly sorted, do not use quick sort!

space complexity is constant O (1)

optimizations - run both halves at the same time
rather than look at the last element, take the median of the last few elements

[4,1,3,9,14,21,20,25,21]

https://visualgo.net/en/sorting


def partition(xs, start, end):
    follower = leader = start
    while leader < end:
        if xs[leader] <= xs[end]:
            xs[follower], xs[leader] = xs[leader], xs[follower]
            follower += 1
        leader += 1
    xs[follower], xs[end] = xs[end], xs[follower]
    return follower

def _quicksort(xs, start, end):
    if start >= end:
        return
    p = partition(xs, start, end)
    _quicksort(xs, start, p-1)
    _quicksort(xs, p+1, end)

def quicksort(xs):
    _quicksort(xs, 0, len(xs)-1)
