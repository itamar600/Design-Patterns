class ListNode:
    def __init__(self, val) -> None:
        """
        Constructor for ListNode.

        Args:
            val: Value to be stored in the node.
        """
        self.val = val  # Value stored in the node
        self.next = None  # Pointer to the next node in the linked list

class LinkedList:
    def __init__(self, head) -> None:
        """
        Constructor for LinkedList.

        Args:
            head: The head node of the linked list.
        """
        self.head = head  # Head node of the linked list
        self.cur = None  # Current node used for iteration

    def __iter__(self):
        """Method to initialize the iterator."""
        self.cur = self.head  # Set current node to the head
        return self

    def __next__(self):
        """Method to get the next node during iteration."""
        if self.cur:  # If current node exists
            val = self.cur.val  # Get the value of the current node
            self.cur = self.cur.next  # Move to the next node
            return val  # Return the value
        else:
            raise StopIteration  # If current node is None, raise StopIteration

# Creating a linked list with nodes 1 -> 2 -> 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Creating a LinkedList object
myList = LinkedList(head)

# Iterating through the linked list and printing each node's value
for n in myList:
    print(n)
