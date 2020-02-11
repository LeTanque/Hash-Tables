import random


def how_many_before_collision(buckets, loops=1):
    # run loops num of times
    for i in range(loops):
        tries = 0
        tried = set()
        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            if hash_index not in tried:
                tried.add(hash_index)
                tries += 1
            else:
                # We have a collision
                break
        print(f"{buckets} buckets, {tries} hashes before collisions. \
({tries / buckets * 100: .1f} %)")


how_many_before_collision(32, 10)


def longest_linked_list_chain(keys, buckets, loops=10):
    # Each key is random
    # Number of buckets is fixed
    # Number of loops is fixed
    #
    # Rolls keys number of random keys into buckets buckets
    # Count the collisions
    # Run loops times
    #
    # If a collision happens, we need to use linked list
    # chaining to fix it
    #
    # # More loops means more chances to get values in buckets
    #
    for init_loop in range(loops):
        key_counts = {}
        #
        # Buckets start with value == 0
        # # More buckets means less end value in each bucket
        #
        for bucket in range(buckets):
            key_counts[bucket] = 0
        #
        # For each key
        # Create random number between 0 and 1
        # Hash the number creating a really big or really small number
        # Store the modulo buckets of hash in hash_index
        # At some pseudo random hash_index, at a value to the bucket
        #
        # # More keys means more values to put in buckets
        #
        for key in range(keys):
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            key_counts[hash_index] += 1

        largest_n = 0

        # key_counts is a dict that stores all of the buckets (key:value)
        # Loop over that dict
        # Store the biggest key as largest_n
        for key in key_counts:
            if key_counts[key] > largest_n:
                largest_n = key_counts[key]

        print(f"Longest Linked list chain for {keys} keys in {buckets} \
buckets (Load factor:{keys / buckets: .3f}) Largest_n: {largest_n}")


longest_linked_list_chain(10, 12, 20)
