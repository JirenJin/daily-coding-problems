"""
Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
"""


def invert_binary_tree(root):
    if root is None:
        return None
    left = invert_binary_tree(root.left)
    right = invert_binary_tree(root.right)
    root.left = right
    root.right = left
    return root
