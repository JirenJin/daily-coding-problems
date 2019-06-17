"""
Given the root of a binary tree, return a deepest node.
For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
"""


import collections


# the deepest node is actually the farthest node from the root
# so we can simply use a BFS traversal and return the last node visited
def find_deepest_node_bfs(root):
    if root is None:
        return None
    queue = collections.deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return node


# DFS version
def find_deepest_node_dfs(root):
    if root is None:
        return None
    deepest_node = root
    max_depth = 0
    def dfs(node, depth):
        nonlocal deepest_node
        nonlocal max_depth
        if node is None:
            return
        if node.left is None and node.right is None:
            if depth > max_depth:
                max_depth = depth
                deepest_node = node
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
    dfs(root, 0)
    return deepest_node


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


if __name__ == "__main__":
    root = TreeNode('a')
    root.left = TreeNode('b')
    root.right = TreeNode('c')
    root.left.left = TreeNode('d')
    print(find_deepest_node_bfs(root).val)
    print(find_deepest_node_dfs(root).val)
