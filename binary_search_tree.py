Binary Search Tree:

Search is the height of the Tree - O (log(n))
Insertion - same process - eventually hit open spot in tree

Unbalanced tree - distribution is skewed

Worst Case scenario for BST -
Search, Insertion, Deletion are all linear time O(n)

        4
      /   \
     2      5
    / \
   1   3

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        node = self.root
        prev_node = self.root
        # chain we need : tree.root.left.right
        while node:
            value = node.value
            if new_val > value:
                prev_node = node
                node = node.right
            elif new_val < value:
                prev_node = node
                node = node.left
        # print value, new_val
        # print tree.root.left == node
        # the connection between this node variable and the insert method of the tree instance is messed up
        new = Node(new_val)
        node = new
        # if prev_node.value < new_val:
        #     prev_node.right = new
        # else:
        #     prev_node.left = new
        # print node.value
        # print tree.root.left.value

    def add_node(self, new_val, node, direction):
    #   print tree.root.value
       node[direction] = Node(new_val)

    def search(self, find_val):
        return False

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
# tree.insert(1)

# tree.insert(3)
# tree.insert(5)
print tree.root.value
print tree.root.left
# print tree.root.left.left.value
# print tree.root.left.right.value
# print tree.root.right.value

# Check search
# Should be True
# print tree.search(4)
# Should be False
# print tree.search(6)
