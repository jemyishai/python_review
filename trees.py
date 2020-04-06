#trees

preliminary points from Udacity:
-Tree can be thought of as an linked list because the structure containing the value has a pointer to the next structure
-In diagrams, linked lists are drawn horizontally and trees are drawn vertically, with root at the top
-trees must be compltely connected
-No CYCLES (as in a graph) no way to travel back to the same node/ even if the direction of an edge doesn't necesarily enable a cycle, if two nodes have an edge to the same child node, it's no longer a tree

Terms:
NODE - individual elements contain values
Root - is the main element
Level - how many connections it takes the root + 1; ie Root is 1, next child down is 2, etc etc
Parent/Child/Descendant/Sibling - logical when viewing in a diagrams
  - children can only have one parent
  - a node can be both child & parent at the same time
  -multiple children of a node are siblings
  -nodes at the end, without children are called leaves or external nodes
    -parent node is an internal node
Edges - connections between nodes
Path - a group of egdes
Height (of a node) - number of edges between it and the furthest leaf on the tree
  -Leaf has a height of 0, but the parent of a leaf has a height of 1
  -Height of a tree overall is just the root node
Depth (of a node)- is the number of edges to the root
 Height & depth should move inversely
  ie, if a node is closer to a leaf than its further from the root
Perfect Tree - every node has two chidren

Traversal:
  Depth-First Search - Going to a leaf
    Pre-Order - Check off Node as you see it before you traverse further down;
      ie ROOT, (left by convention), and then check off further children
    In-Order - TRaversing down until you hit a leaf. Truly LEFT-TO-RIGHT
    Post-Order - All children, left-to-right, then parents of those children
  Breadth-First Search - Level by level
    -Level Order - start left most side and go right

    TREE Traversal - Write out the order nodes would visited in post-order traversal. (Exactly like "X,Y,Z")
                            "A"
                          /     \
                         "B"    "C"
                         /        \
                        "D"       "E"
                                    \
                                    "F"
    D,F,E,B,C,A

Standard Trees (no order):
      Search - is O(n)
      Delete is O(n)


Insertion (when it has no order)
 every level has O(logN) insertion time
 each new level can have 2X nodes as the one before it


   Binary Trees:
      Parents have two children
