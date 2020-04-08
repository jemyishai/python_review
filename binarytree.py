  Binary Tree Practice
            1
          /  \
         2     3
        /       \
       4         5

##one of the larger issues is that I'm not familiar with the self

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        struggle_train = self.preorder_search(self.root,find_val)
        print struggle_train
        # if output == True:
        #     return True
        # else:
        #     return False

    def print_tree(self):
        output_string = ''
        output_array = self.preorder_print(self.root,[])
        for item in output_array:
            output_string = output_string + str(item) + "-"
        print output_string[:-1]


    def preorder_search(self, start, find_val):
        if start.left == None and start.right == None:
            # print start.value, find_val
            if start.value == find_val:
                print 'made it here'
                return 58
        elif start.left != None:
            # print start.value
            if start.value == find_val:
                return True
            else:
                self.preorder_search(start.left, find_val)
                self.preorder_search(start.right,find_val)
        elif start.right != None:
            if start.value == find_val:
                return True
            else:
                self.preorder_search(start.right, find_val)
                self.preorder_search(start.left,find_val)


    def preorder_print(self, start, traversal):
        node = start
        if node.left == None and node.right == None:
            traversal.append(node.value)
        elif node.left != None:
            traversal.append(node.value)
            self.preorder_print(node.left, traversal)
            self.preorder_print(node.right,traversal)
        elif node.right != None:
            traversal.append(node.value)
            self.preorder_print(node.right, traversal)
            self.preorder_print(node.left, traversal)
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()
