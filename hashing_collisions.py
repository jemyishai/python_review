# Hashing Functions are O(1) for info retrieval

# When we're talking about hash tables, we can define a "load factor":

# Load Factor = Number of Entries / Number of Buckets
100/
5
25

# The purpose of a load factor is to give us a sense of how "full" a hash table is. For example, if we're trying to store 10 values in a hash table with 1000 buckets, the load factor would be 0.01, and the majority of buckets in the table will be empty. We end up wasting memory by having so many empty buckets, so we may want to rehash, or come up with a new hash function with less buckets. We can use our load factor as an indicator for when to rehash—as the load factor approaches 0, the more empty, or sparse, our hash table is.

# On the flip side, the closer our load factor is to 1 (meaning the number of values equals the number of buckets), the better it would be for us to rehash and add more buckets. Any table with a load value greater than 1 is guaranteed to have collisions.

One of your coworkers comes to you with a hash function that divides a group of values by 100, and uses the remainder as a key. The values are 100 numbers that are all multiples of 5.

This is a very poorly worde question because one has to infer that there are 100 buckets (0-99) based on the first clause "that divides a group of values by 100 and uses the remainder as a key." The second sentence makes one think that the there are only 25 buckets becasue the "remainder" mentioned in the first sentence would be limited to the given data set. But its not clear that this is a poorly constructed to hash function (though maybe that's not true because a later sentence does decribe it running slowly), and the two sentences are not related to each other.


Answer below:
For the load factor, you should divide the number of values by the number of buckets. There are 100 values, as stated in the question, and 100 buckets (0 to 99). Thus, 100/100 = 1!

The answer to the second part is 107. The other values all had something wrong with them:

125 is also a multiple of 5. Dividing a bunch of multiples of 5 by another multiple of 5 will cause a lot of collisions. Here's an example, where 10 is used as the divisor:
5 % 10 = 5
10 % 10 = 0
15 % 10 = 5
20 % 10 = 0
87 is better than 125, but because it's less than 100 it'll still have collisions.
1001 is good, but it'll create a ton of leftover buckets and waste a lot of memory.

Java convention stems from historical use of number 31 - https://stackoverflow.com/questions/299304/why-does-javas-hashcode-in-string-use-31-as-a-multiplier


#######################################
# STRING KEYS PRACTICE:
# In this quiz, you'll write your own hash table and hash function that uses string keys. Your table will store strings in buckets by their first two letters, according to the formula below:

# Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter
# You can assume that the string will have at least two letters, and the first two characters are uppercase letters (ASCII values from 65 to 90). You can use the Python function ord() to get the ASCII value of a letter, and chr() to get the letter associated with an ASCII value.

# You'll create a HashTable class, methods to store and lookup values, and a helper function to calculate a hash value given a string. You cannot use a Python dictionary—only lists! And remember to store lists at each bucket, and not just the string itself. For example, you can store "UDACITY" at index 8568 as ["UDACITY"].


HASH TABLE CLASS:
"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        index = self.calculate_hash_value(string)
        self.table[index] = [string]
        pass

    def lookup(self, string):
        index = self.calculate_hash_value(string)
        if self.table[index] != None:
            return index
        else:
            return -1
# Hash Value = (ASCII Value of First Letter * 100) + ASCII Value of Second Letter
# You can use the Python function ord() to get the ASCII value of a letter, and chr()
    def calculate_hash_value(self, string):
        return ord(string[0])*100+ord(string[1])
        """Helper function to calulate a
        hash value from a string."""


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')


####ANSWER ACCOUTING FOR COLLISIONS:
class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]

    def lookup(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                if string in self.table[hv]:
                    return hv
        return -1

    def calculate_hash_value(self, string):
        value = ord(string[0])*100 + ord(string[1])
        return value
