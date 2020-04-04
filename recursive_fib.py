"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

def get_fib(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return get_fib(position-2)+get_fib(position-1)
    return -1

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)


# Here's the recursive solution:

# def get_fib(position):
#     if position == 0 or position == 1:
#         return position
#     return get_fib(position - 1) + get_fib(position - 2)
# Isn't that elegant? We took a short function and managed to write it in even fewer lines!

# Apparently Google thinks recursion is pretty cool too—if you search for "recursion" in Google's search engine, the first thing that pops up is "Did you mean: recursion". Don't get stuck in an infinite loop continuously searching "recursion"!

# You may have noticed that this solution will compute the values of some inputs more than once. For example get_fib(4) calls get_fib(3) and get_fib(2), get_fib(3) calls get_fib(2) and get_fib(1) etc. The number of recursive calls grows exponentially with n.

# In practice if we were to use recursion to solve this problem we should use a hash table to store and fetch previously calculated results. This will increase the space needed but will drastically improve the runtime efficiency.