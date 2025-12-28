from collections import deque
from typing import Optional
from lc150.tree.tree_node import TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    def maxDepth_DFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
    
    def maxDepth_BFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        level = 0
        while queue:
            levelSize = len(queue)
            for i in range(levelSize):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level