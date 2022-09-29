# A linked list is a sequence of data elements, which are connected together via links. Each data element contains a connection to another data element in form of a pointer.
# In creation of the linked list ~ We create a Node object and create another class to use this ode object. We pass the appropriate values through the node object to point the to the next data elements.

# in python code ~ for the creation of linked list
class IGLinkedList:
  def __init__(self):
    self.data = data
    self.next = None
    
class LinkedList:

    def __init__(self):
        self.head = None


if __name__ == '__main__':

    linked_list = LinkedList()

    # Assign item values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Connect nodes
    linked_list.head.next = second
    second.next = third

    # Print the linked list item
    while linked_list.head != None:
        print(linked_list.head.item, end=" ")
        linked_list.head = linked_list.head.next
    
