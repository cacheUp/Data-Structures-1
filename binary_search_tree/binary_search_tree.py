import sys
sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
                print(self.left)
                return
            else:
                self.left.insert(value)
        elif value > self.value or value == self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
                return
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value:
            print(self.value, self.right)
            if self.right == None:
                return False
            elif target == self.right.value:
                return True
            else:
                return self.right.contains(target)
        if target < self.value:
            if self.left == None:
                return False
            elif target == self.left.value:
                return True
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(5)
# bst.insert(1)
# print(bst.right.value)


bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(6)
bst.insert(300)
print(bst.left.right.value)
print(bst.right.left.value)
print(bst.get_max())
