
Hash_Theory = """

We use a special function that turns data like the string “Joan McNeil” into a number. This function is called a hashing function, or a hash function. 
 Hashing functions are useful in many domains, but for our data structure the most important aspect is that a hashing function returns an array index as output.

A hash map with a linked list separate chaining strategy follows a similar flow to the hash maps that have been described so far.
 The user wants to assign a value to a key in the map. The hash map takes the key and transforms it into a hash code.
  The hash code is then converted into an index to an array using the modulus operation. If the value of the array at the hash function’s returned index is empty, a new linked list is created with the value as the first element of the linked list. If a linked list already exists at the address, append the value to the linked list given.

This is effective for hash functions that are particularly good at giving unique indices, so the linked lists never get very long.
 But in the worst-case scenario, where the hash function gives all keys the same index, lookup performance is only as good as it would be on a linked list.
  Hash maps are frequently employed because looking up a value (for a given key) is quick. Looking up a value in a linked list is much slower than a perfect, collision-free hash map of the same size. A hash map that uses separate chaining with linked lists but experiences frequent collisions loses one of its most essential features.

Open Addressing: Linear Probing:
	A hash map with a linked list separate chaining strategy follows a similar flow to the hash maps that have been described so far.
	 The user wants to assign a value to a key in the map. The hash map takes the key and transforms it into a hash code. 
	  The hash code is then converted into an index to an array using the modulus operation. 
	   If the value of the array at the hash function’s returned index is empty, a new linked list is created with the value as the first element of the linked list. 
    	If a linked list already exists at the address, append the value to the linked list given.
	This is effective for hash functions that are particularly good at giving unique indices, so the linked lists never get very long.
	 But in the worst-case scenario, where the hash function gives all keys the same index, lookup performance is only as good as it would be on a linked list.
	  Hash maps are frequently employed because looking up a value (for a given key) is quick.
	   Looking up a value in a linked list is much slower than a perfect, collision-free hash map of the same size.
	    A hash map that uses separate chaining with linked lists but experiences frequent collisions loses one of its most essential features.
"""

# Basic HashMap


class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    self.array[array_index] = value

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    return self.array[array_index]

  
hash_map = HashMap(20)

hash_map.assign('gneiss', 'metamorphic')
print(hash_map.retrieve('gneiss'))







# Collision and Open Addressing

class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    # updating for No key
    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    # updating for same key
    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # Collision!

    number_collisions = 1

    while(current_array_value[0] != key):
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]

      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return

      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return

      number_collisions += 1

    return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    # no key
    if possible_return_value is None:
        return None

    # same key
    if possible_return_value[0] == key:
      return possible_return_value[1]

    # possible_return_value holds different key
    retrieval_collisions = 1
    while possible_return_value[0] != key:
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]

      if possible_return_value is None:
        return

      # same key
      if possible_return_value[0] == key:
        return possible_return_value[1]

      # different key
      retrieval_collisions += 1


      
hash_map = HashMap(15)

hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')

# retreiving

print(hash_map.retrieve('gabbro'))
print(hash_map.retrieve('sandstone'))
print(hash_map.retrieve('gneiss'))



# How would you delete a key-value pair from this hash map?
# Parts of the code are a little repetitive, how would you factor these roles differently?
# What should your hash map do if a key-value is added and the array is full? How does this hash map handle that?
      
      
      
      

