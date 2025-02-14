
# Defines a node in the singly linked list
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Defines the singly linked list


class LinkedList:
    def __init__(self):
        self.head = None  # keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)

    def get_first(self):
        if self.head is None:
            return None
        return self.head.value

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        return self.head.value

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def search(self, value):
        if self.head is None:
            return False
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def length(self):
        # edge case - empty list
        if self.head is None:
            return 0
        # list is not empty
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        current_node = self.get_node_at_index(index)
        return current_node.value if current_node else None

    def get_node_at_index(self, index):
        if index > self.length() - 1:
            return None
        current_node = self.head
        current_index = 0
        while current_index < index:
            current_index += 1
            current_node = current_node.next
        return current_node

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if self.head is None:
            return None
        list_length = self.length()
        return self.get_node_at_index(list_length - 1).value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def add_last(self, value):
        node_to_add_last = Node(value)

        # empty list
        if self.head is None:
            self.head = node_to_add_last
            return

        current_node = self.head
        while current_node is not None:
            if current_node.next is None:
                current_node.next = node_to_add_last
                return
            current_node = current_node.next

    # method to return the max value in the linked list
    # returns the data value and not the node
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def find_max(self):
        if self.head is None:
            return

        current_node = self.head
        max = current_node.value
        while current_node is not None:
            current_node = current_node.next
            if current_node is not None and current_node.value > max:
                max = current_node.value
        return max

    # method to delete the first node found with specified value
    # Time Complexity: O(n)
    # Space Complexity: O(1)

    def delete(self, value):
        # empty list edge case
        if self.head is None:
            return

        # edge case - first node value = to target value
        if self.head.value == value:
            self.head = self.head.next

        current_node = self.head
        while current_node is not None and current_node.next is not None:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next

        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
        # empty list - do nothing
        if self.head is None:
            return

        # just one element in a list - do nothing
        if self.head.next is None:
            return

        prev_node = None
        current_node = self.head
        next_node = current_node.next

        while True:
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            if next_node is not None:
                next_node = next_node.next
            else:
                break

        self.head = prev_node

    # Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: ?
    # Space Complexity: ?

    def find_middle_value(self):
        pass

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: ?
    # Space Complexity: ?
    def find_nth_from_end(self, n):
        pass

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: ?
    # Space Complexity: ?
    def has_cycle(self):
        pass

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head is None:
            return

        # navigate to last node
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = self.head  # make the last node link to first node
