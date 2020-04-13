Self-Balancing Trees Notes:

-Unbalanced tree has nodes spread out among many levels

            4
              \
                5
              /   \
              3    2
                    \
                    7

Linked List is the ultimate unbalanced tree because every node has only one child

Balanced Tree has nodes condensed to only a few levels
                                15
                              /   \
                             6     22
                           /  \   /  \
                          3    8 18   36

-Self balancing tree has nodes condensed to only a few levels
  -minimizes the # of levels that it use:
    algorithm during insertion and deletion to keep itself balanced and the nodes themselves may have additional properties
    For example, a red-black tree (a type of binary search tree)

    Red-Black Tree:
      1)-Each Node is assigned a color property where the nodes must be either red or black
        -Use of color as red or black is just convention to distinguish between two different types of nodes
      2)-Existence of null leaf nodes:
            Every node that doesn't have two leaves must have null children
            -All null children must be black
            -All null leaf nodes must be black
      3) If a node is red both of its children must be black
      4) (Optional, this rule is not mandatory for red-black trees) The root node must be black
      5) In order to be useful, every path from the root to its descendant null nodes must contain the same number of black nodes
    All these rules assure the tree is not unbalanced.


  Insertion into a Red-Black Tree




