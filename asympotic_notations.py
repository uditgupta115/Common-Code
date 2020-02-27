"""

Sometimes, a program may have a different runtime for the best case and worst case.
For instance, a program could have a best case runtime of Θ(1) and a worst case of Θ(N).
We use a different notation when this is the case. We use big Omega or Ω to describe the
 best case and big O or O to describe the worst case. 

"""
# Asympotic Notations Examples:

# -----------------------------Analyse the Run Time--------------------------------- #


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


# ----------------------------Finding Max Value in LinkedList------------------------------- #


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



# --------------------------------Sorting the Linked List------------------------------------ #


from linkedlist import LinkedList

def find_max(linked_list):
  current = linked_list.get_head_node()
  maximum = current.get_value()
  while current.get_next_node():
    current = current.get_next_node()
    val = current.get_value()
    if val > maximum:
      maximum = val
  return maximum

#Fill in Function
def sort_linked_list(linked_list):
  print("\n---------------------------")
  print("The original linked list is:\n{0}".format(linked_list.stringify_list()))
  new_linked_list = LinkedList()
  #Write Code Here!
  while linked_list.head_node:
    max_value = find_max(linked_list)
    new_linked_list.insert_beginning(max_value)
    node = linked_list.remove_node(max_value)
  return new_linked_list

  

#Test Cases
ll = LinkedList("Z")
ll.insert_beginning("C")
ll.insert_beginning("Q")
ll.insert_beginning("A")
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll).stringify_list()))

ll_2 = LinkedList(1)
ll_2.insert_beginning(4)
ll_2.insert_beginning(18)
ll_2.insert_beginning(2)
ll_2.insert_beginning(3)
ll_2.insert_beginning(7)
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll_2).stringify_list()))

ll_3 = LinkedList(-11)
ll_3.insert_beginning(44)
ll_3.insert_beginning(118)
ll_3.insert_beginning(1000)
ll_3.insert_beginning(23)
ll_3.insert_beginning(-92)
print("The sorted linked list is:\n{0}".format(sort_linked_list(ll_3).stringify_list()))

#Runtime
runtime = "N^2"
print("The runtime of sort_linked_list is O({0})\n\n".format(runtime))



# --------------------------------Sorting the Linked List------------------------------------ #


from stack import Stack
from queue import Queue

N = 6

my_stack = Stack(N)
my_stack.push("Australia")
my_stack.push("India")
my_stack.push("Costa Rica")
my_stack.push("Peru")
my_stack.push("Ghana")
my_stack.push("Indonesia")

my_queue = Queue(N)
my_queue.enqueue("Australia")
my_queue.enqueue("India")
my_queue.enqueue("Costa Rica")
my_queue.enqueue("Peru")
my_queue.enqueue("Ghana")
my_queue.enqueue("Indonesia")

#Print the first values in the stack and queue
print("The top value in my stack is: {0}".format(my_stack.peek()))
print("The front value of my queue is: {0}".format(my_queue.peek()))

#Get First Value added to Queue
first_value_added_to_queue = my_queue.dequeue() #Checkpoint 2
print("\nThe first value enqueued to the queue was {0}".format(first_value_added_to_queue))
queue_runtime = "1" #Checkpoint 3
print("The runtime of getting the front of the queue is O({0})".format(queue_runtime))

#Get First Value added to Stack
#Write Code Here for #Checkpoint 4
for i in range(my_stack.size):
  if my_stack.size == 1:
    first_value_added_to_stack = my_stack.pop()
  else:
    my_stack.pop()

print("\nThe first value pushed onto the stack was {0}".format(first_value_added_to_stack))
stack_runtime = "N" #Checkpoint 5
print("The runtime of getting the bottom of the stack is O({0})".format(stack_runtime))



# - -------------------------HashMaps vs. Linked Lists Runtime------------------------------- #


from hashmap import HashMap
from linkedlist import LinkedList

N = 6

#Insert Data Into HashMap
my_hashmap = HashMap(N)
my_hashmap.assign("Zachary", "Sunburn Sickness")
my_hashmap.assign("Elise", "Severe Nausea")
my_hashmap.assign("Mimi", "Stomach Flu")
my_hashmap.assign("Devan", "Malaria")
my_hashmap.assign("Gary", "Bacterial Meningitis")
my_hashmap.assign("Neeknaz", "Broken Cheekbone")

#Insert Data into LinkedList
my_linked_list = LinkedList(["Zachary", "Sunburn Sickness"])
my_linked_list.insert_beginning(["Elise", "Severe Nausea"])
my_linked_list.insert_beginning(["Mimi", "Stomach Flu"])
my_linked_list.insert_beginning(["Devan", "Malaria"])
my_linked_list.insert_beginning(["Gary", "Bacterial Meningitis"])
my_linked_list.insert_beginning(["Neeknaz", "Broken Cheekbone"])

#Get Zachary's Disease from a HashMap
hashmap_zachary_disease = my_hashmap.retrieve("Zachary")
print("Zachary's disease is {0}".format(hashmap_zachary_disease))
hashmap_runtime = "1"
print("The runtime of retrieving a value from a hashmap is O({0})\n\n".format(hashmap_runtime))


#Get Zachary's Disease from a Linked List
traverse = my_linked_list.get_head_node()
while traverse.get_value()[0] != "Za1chary":
  traverse = traverse.get_next_node()
linked_list_zachary_disease = traverse.get_value()[1]
print("Zachary's disease is {0}".format(linked_list_zachary_disease))
linked_list_runtime = "N"
print("The runtime of retrieving the first value added to a linked list is O({0})\n\n".format(linked_list_runtime))




# ----------------------------------------End------------------------------------------------ #
