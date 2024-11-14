# The following struct defines the node of a binary tree:
class BinaryTreeNode:
    def __init__(self, info):
        self.info = info       # Stores the node's data
        self.llink = None      # Pointer to the left child
        self.rlink = None      # Pointer to the right child


# The general algorithm to find the height of a binary tree is as follows. Suppose height(p) denotes the height of the binary tree with root p.
def height(node):
    if node is None:
        return 0
    else:
        return 1 + max(height(node.llink), height(node.rlink))

# Clearly, this is a recursive algorithm. The following function implements this algorithm:
def height(node):
    if node is None:
        return 0
    else:
        return 1 + max(height(node.llink), height(node.rlink))


# COPY TREE
# Given a pointer to the root node of a binary tree,
# we next describe the function copyTree,
# which makes a copy of a given binary tree.
# This function is also useful in implementing the copy constructor and overloading the assignment operator.
def copy_tree(other_tree_root):
    if other_tree_root is None:
        return None
    else:
        copied_tree_root = BinaryTreeNode(other_tree_root.info)
        copied_tree_root.llink = copy_tree(other_tree_root.llink)
        copied_tree_root.rlink = copy_tree(other_tree_root.rlink)
        return copied_tree_root


# Binary Tree Operation
# Insert Operation
# Algorithm
class BinaryTreeNode:
    def __init__(self, info):
        self.info = info
        self.llink = None
        self.rlink = None


def insert(root, data):
    # If root is None, create the root node
    if root is None:
        return BinaryTreeNode(data)

    # Initialize the current node as root
    current = root

    # Loop until the correct insertion position is found
    while True:
        # If data is greater than the current node's info, go to the right subtree
        if data > current.info:
            # If there is no right child, insert here
            if current.rlink is None:
                current.rlink = BinaryTreeNode(data)
                break
            else:
                current = current.rlink  # Move to the right child
        else:
            # If there is no left child, insert here
            if current.llink is None:
                current.llink = BinaryTreeNode(data)
                break
            else:
                current = current.llink  # Move to the left child

    return root  # Return the unchanged root of the tree


# Implementation
# The implementation of insert function should look like this −
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Create a new node
        temp_node = BinaryTreeNode(data)

        # If the tree is empty, set the new node as the root
        if self.root is None:
            self.root = temp_node
        else:
            # Initialize current and parent pointers
            current = self.root
            parent = None

            while True:
                parent = current

                # Go to the left subtree
                if data < parent.data:
                    current = current.leftChild

                    # If no left child, insert here
                    if current is None:
                        parent.leftChild = temp_node
                        return

                # Go to the right subtree
                else:
                    current = current.rightChild

                    # If no right child, insert here
                    if current is None:
                        parent.rightChild = temp_node
                        return


# Search Operation
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def search(self, data):
        current = self.root
        print("Visiting elements: ", end="")

        while current is not None:
            print(current.data, end=" ")

            # If the current node's data matches the search data, return the node
            if current.data == data:
                return current

            # Go to the left subtree if data is less than the current node's data
            if current.data > data:
                current = current.leftChild
            # Go to the right subtree if data is greater than the current node's data
            else:
                current = current.rightChild

        # If data not found, return None
        print()  # For newline after visiting elements
        return None


# The implementation of tree traversal
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        tempNode = Node(data)

        # If the tree is empty, set root to new node
        if self.root is None:
            self.root = tempNode
        else:
            current = self.root
            parent = None

            while True:
                parent = current

                # Insert on the left subtree
                if data < parent.data:
                    current = current.leftChild

                    # Insert here if no child
                    if current is None:
                        parent.leftChild = tempNode
                        return
                # Insert on the right subtree
                else:
                    current = current.rightChild

                    # Insert here if no child
                    if current is None:
                        parent.rightChild = tempNode
                        return

    def search(self, data):
        current = self.root
        print("Visiting elements: ", end="")

        while current is not None:
            print(current.data, end=" ")
            if current.data == data:
                return current
            elif data < current.data:
                current = current.leftChild
            else:
                current = current.rightChild

        return None  # Element not found

    def pre_order_traversal(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.pre_order_traversal(root.leftChild)
            self.pre_order_traversal(root.rightChild)

    def inorder_traversal(self, root):
        if root is not None:
            self.inorder_traversal(root.leftChild)
            print(root.data, end=" ")
            self.inorder_traversal(root.rightChild)

    def post_order_traversal(self, root):
        if root is not None:
            self.post_order_traversal(root.leftChild)
            self.post_order_traversal(root.rightChild)
            print(root.data, end=" ")

# Usage
bst = BinarySearchTree()
elements = [27, 14, 35, 10, 19, 31, 42]

# Insert elements
for elem in elements:
    bst.insert(elem)

# Search for an element
element_to_search = 31
result = bst.search(element_to_search)
if result is not None:
    print(f"\n[{result.data}] Element found.")
else:
    print(f"\n[ x ] Element not found ({element_to_search}).")

# Search for an element not in the tree
element_to_search = 15
result = bst.search(element_to_search)
if result is not None:
    print(f"\n[{result.data}] Element found.")
else:
    print(f"\n[ x ] Element not found ({element_to_search}).")

# Traversals
print("\nPreorder traversal: ", end="")
bst.pre_order_traversal(bst.root)

print("\nInorder traversal: ", end="")
bst.inorder_traversal(bst.root)

print("\nPostorder traversal: ", end="")
bst.post_order_traversal(bst.root)


# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


# Insert Operation
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # Create a new node
        tempNode = Node(data)

        # If the tree is empty, set the root to the new node
        if self.root is None:
            self.root = tempNode
        else:
            current = self.root
            parent = None

            while True:
                parent = current

                # Go to the left of the tree
                if data < parent.data:
                    current = current.leftChild

                    # Insert to the left if there is no left child
                    if current is None:
                        parent.leftChild = tempNode
                        return
                # Go to the right of the tree
                else:
                    current = current.rightChild

                    # Insert to the right if there is no right child
                    if current is None:
                        parent.rightChild = tempNode
                        return
