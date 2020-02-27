# Conceptuals:
"""
Recursion has two fundamental aspects: the base case and the recursive step.

When using iteration, we rely on a counting variable and a boolean condition. For example, when iterating through the values in a list, we would increment the counting variable until it exceeded the length of the dataset.

Recursive functions have a similar concept, which we call the base case. The base case dictates whether the function will recurse, or call itself. Without a base case, it’s the iterative equivalent to writing an infinite loop.

Because we’re using a call stack to track the function calls, your computer will throw an error due to a stack overflow if the base case is not sufficient.

The other fundamental aspect of a recursive function is the recursive step. This portion of the function is the step that moves us closer to the base case.

In an iterative function, this is handled by a loop construct that decrements or increments the counting variable which moves the counter closer to a boolean condition, terminating the loop.

In a recursive function, the “counting variable” equivalent is the argument to the recursive call. If we’re counting down to 0, for example, our base case would be the function call that receives 0 as an argument. We might design a recursive step that takes the argument passed in, decrements it by one, and calls the function again with the decremented argument. In this way, we would be moving towards 0 as our base case.

Analyzing the Big O runtime of a recursive function is very similar to analyzing an iterative function. Substitute iterations of a loop with recursive calls.

For example, if we loop through once for each element printing the value, we have a O(N) or linear runtime. Similarly, if we have a single recursive call for each element in the original function call, we have a O(N) or linear runtime.

----------------------------------------------------------------------------------------------------

With an iterative function, we would consider how the number of iterations grows in relation to the size of the input.

For example you may ask yourself, are we looping once more for each new element in the list?

That’s linear or O(N).

Are we looping an additional number of elements in the list for each new element in the list?

That’s quadratic or O(N^2).

With recursive functions, the thought process is similar but we’re replacing loop iterations with recursive function calls.

In other words, are we recursing once more for each new element in the list?

That’s linear or O(N).

----------------------------------------------------------------------------------------------------

every recursive call spends time on the call stack.

Put enough function calls on the call stack, and eventually there’s no room left.

Even when there is room for any reasonable input, recursive functions tend to be at least a little less efficient than comparable iterative solutions because of the call stack.

The beauty of recursion is how it can reduce complex problems into an elegant solution of only a few lines of code. Recursion forces us to distill a task into its smallest piece, the base case, and the smallest step to get there, the recursive step.

Let’s compare two solutions to a single problem: producing a power set. A power set is a list of all subsets of the values in a list.

This is a really tough algorithm. Don’t be discouraged! 

----------------------------------------------------------------------------------------------------

Recursive Data Structures

Data structures can also be recursive.

Trees are a recursive data structure because their definition is self-referential. A tree is a data structure which contains a piece of data and references to other trees!

Trees which are referenced by other trees are known as children. Trees which hold references to other trees are known as the parents.

A tree can be both parent and child. We’re going to write a recursive function that builds a special type of tree: a binary search tree.

Binary search trees:

    Reference two children at most per tree node.
    The “left” child of the tree must contain a value lesser than its parent
    The “right” child of the tree must contain a value greater than its parent.

Trees are an abstract data type, meaning we can implement our version in a number of ways as long as we follow the rules above.

For the purposes of this exercise, we’ll use the humble Python dictionary:

bst_tree_node = {"data": 42}
bst_tree_node["left_child"] = {"data": 36}
bst_tree_node["right_child"] = {"data": 73}

bst_tree_node["data"] > bst_tree_node["left_child"]["data"]
# True
bst_tree_node["data"] < bst_tree_node["right_child"["data"]
# True

We can also assume our function will receive a sorted list of values as input.

This is necessary to construct the binary search tree because we’ll be relying on the ordering of the list input.

Our high-level strategy before moving through the checkpoints.

    base case: the input list is empty
        Return "No Child" to represent the lack of node
    recursive step: the input list must be divided into two halves
        Find the middle index of the list
        Store the value located at the middle index
        Make a tree node with a "data" key set to the value
        Assign tree node’s "left child" to a recursive call using the left half of the list
        Assign tree node’s "right child" to a recursive call using the right half of the list
        Return the tree node

"""


# Recursion behind the scenes

def sum_to_one(n):
  result = 1
  call_stack = []
  
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")
  while call_stack:
    return_value = call_stack.pop()
    print(call_stack)
    print(return_value['n_value'])
    result += return_value['n_value']
  return result, call_stack

sum_to_one(4)



# Example 2
# define flatten() below...


### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

def flatten(my_list):
  result = []
  for i in my_list:
    if isinstance(i, list):
      print("list found!")
      flat_list = flatten(i)
      result.extend(flat_list)
    else:
      result.append(i)
  return result

print(flatten(planets))


# BST DS
# Define build_bst() below...
def build_bst(my_list):
  if not my_list:
    return "No Child"
  middle_idx = len(my_list) // 2
  middle_value = my_list[middle_idx]
  # print("Middle index: " + str(middle_idx))
  # print("Middle value: " + str(middle_value))
  tree_node = {"data": middle_value}
  tree_node['left_child'] = build_bst(my_list[:middle_idx])
  tree_node['right_child'] = build_bst(my_list[middle_idx+1:])
  return tree_node
# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"

# {'data': 14, 'left_child': {'data': 13, 'left_child': {'data': 12, 'left_child': 'No Child', 'right_child': 'No Child'}, 'right_child': 'No Child'}, 'right_child': {'data': 16, 'left_child': {'data': 15, 'left_child': 'No Child', 'right_child': 'No Child'}, 'right_child': 'No Child'}}
