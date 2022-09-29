# A linked list is a sequence of data elements, which are connected together via links. Each data element contains a connection to another data element in form of a pointer.
# In creation of the linked list ~ We create a Node object and create another class to use this ode object. We pass the appropriate values through the node object to point the to the next data elements.

# in python code ~ for the creation of linked list
class IGLinkedList:
  def __init__(self, data):
    self.data = data
    self.next = None
    
# init the head of the linked list
class headLinkedList:
  def __init__(self):
    self.head = None # usually the head did not store any data in it
    
 if __name__== '__main__':
  linked_list = headLinkedList()
  
  # Assign item value for the linked list
  linked_list.head = Node(1)
  second = Node(2)
  third = Node(3)
  
  # connect the nodes
  linked_list.head.next = second
  second.next = third
  
  # print the element in the linkedlist
  while linked_list.head != None:
    print(linked_list.head.item, end = " ")
    linked_list.head = linked_list.head.next
    
