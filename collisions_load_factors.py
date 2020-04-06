Collisions
When Hash value spits out same index for two different inputs
  two main ways:
    BASECS Podcast does a much better job of explaining linear probing that this online course
    Change value in hash function
    change structure in array
      rather than store one value, you can

    Ideally one - three elements in each bucket, so we have that goal in mind when desigining the bucket
      With a few really large buckets, we could have a secondary hash functions for each of the secondary buckets

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
