# Binary Search Tree:

# Search is the height of the Tree - O (log(n))
# Insertion - same process - eventually hit open spot in tree

# Unbalanced tree - distribution is skewed

# Worst Case scenario for BST -
# Search, Insertion, Deletion are all linear time O(n)

#Iterative implementations require pointers to current and previous nodes

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    #iterative solution
    # def insert(self, new_val):
    #     node = self.root
    #     prev_node = self.root
    #     # chain we need : tree.root.left.right
    #     while node:
    #         value = node.value
    #         if new_val > value:
    #             prev_node = node
    #             node = node.right
    #         elif new_val < value:
    #             prev_node = node
    #             node = node.left
    #     # the connection between this node variable and the insert method of the tree instance is messed up
    #     new = Node(new_val)
    #     # node = new
    #     if prev_node.value < new_val:
    #         prev_node.right = new
    #     else:
    #         prev_node.left = new
    #     return tree

    def insert(self, new_val):
        return self.insert_helper(self.root,new_val)

    def insert_helper(self,node,new_val):
        if node.value > new_val:
            if node.left != None:
                self.insert_helper(node.left,new_val)
            else:
                node.left = Node(new_val)
        elif node.value < new_val:
            if node.right != None:
                self.insert_helper(node.right, new_val)
            else:
                node.right = Node(new_val)

    #iterative solution
    # def search(self, find_val):
    #     node = self.root
    #     previous_node = self.root
    #     while node:
    #         if node.value == find_val:
    #             return True
    #         elif node.value < find_val:
    #             previous_node = node
    #             node = node.right
    #         elif node.value > find_val:
    #             previous_node = node
    #             node = node.left
    #     return False

    def search(self, find_val):
        return self.search_help(self.root,find_val)

    def search_help(self,node,find_val):
        if node.value == find_val:
            return True
        elif node.left == None and node.right == None:
            return False
        else:
            return self.search_help(node.left,find_val) or self.search_help(node.right,find_val)

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be Fals
print tree.search(6)
print tree.search(7)
