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


# this problem we only need to traverse each node exactly once and swap its
# left and right children. Therefore we can use any order of traversal.


# post-order traversal
def invert_binary_tree(root):
    if root is None:
        return None
    left = invert_binary_tree(root.left)
    right = invert_binary_tree(root.right)
    root.left = right
    root.right = left
    return root


# pre-order traversal
def invert_binary_tree(root):
    def dfs(root):
        if root:
            root.left, root.right = root.right, root.left
            dfs(root.left)
            dfs(root.right)
    dfs(root)
    return root


# pre-order iterative
def invertTree(self, root: TreeNode) -> TreeNode:
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
    return root


# bfs
def invert_binary_tree(root):
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root
