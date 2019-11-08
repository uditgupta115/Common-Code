# Asympotic Notations Examples:


def count(N):
  count = 0
  while N > 1:
    N = N//2
    count += 1
  return count


num_iterations_1 = count(1) #REPLACE
print("The while loop performs {0} iterations when N is 1".format(num_iterations_1))

num_iterations_2 = count(2) #REPLACE
print("\nThe while loop performs {0} iterations when N is 2".format(num_iterations_2))

num_iterations_4 = count(4) #REPLACE
print("\nThe while loop performs {0} iterations when N is 4".format(num_iterations_4))

num_iterations_32 = count(32) #REPLACE
print("\nThe while loop performs {0} iterations when N is 32".format(num_iterations_32))

num_iterations_64 = count(64) #REPLACE
print("\nThe while loop performs {0} iterations when N is 64".format(num_iterations_64))

runtime = "log N"
print("\nThe runtime for this function is O({0})".format(runtime))


# ---------------------------------------------------------------------------------------------- #


from linkedlist import LinkedList


def find_max(linked_list):
  print("--------------------------")
  print("Finding the maximum value of:\n{0}".format(linked_list.stringify_list()))

  head_node = linked_list.get_head_node()
  if head_node:
    max_value = head_node.get_value()
    while head_node:
      next_node = head_node.get_next_node()
      if next_node and next_node.get_value() > max_value:
        max_value = next_node.get_value()
      head_node = next_node
  return max_value
    
    
  

#Test Cases
ll = LinkedList(6)
ll.insert_beginning(32)
ll.insert_beginning(-12)
ll.insert_beginning(48)
ll.insert_beginning(2)
ll.insert_beginning(1)
print("The maximum value in this linked list is {0}\n".format(find_max(ll)))

ll_2 = LinkedList(60)
ll_2.insert_beginning(12)
ll_2.insert_beginning(22)
ll_2.insert_beginning(-10)
print("The maximum value in this linked list is {0}\n".format(find_max(ll_2)))

ll_3 = LinkedList("A")
ll_3.insert_beginning("X")
ll_3.insert_beginning("V")
ll_3.insert_beginning("L")
ll_3.insert_beginning("D")
ll_3.insert_beginning("Q")
print("The maximum value in this linked list is {0}\n".format(find_max(ll_3)))

#Runtime
runtime = "N"
print("The runtime of find_max is O({0})".format(runtime))

# ---------------------------------------------------------------------------------------------- #



