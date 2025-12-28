from collections import deque
from typing import Optional
from lc150.tree.tree_node import TreeNode

class Solution:
    def invertTree_BFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
    
    def invertTree_Rec(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        leftChild = self.invertTree_Rec(root.right)
        rightChild = self.invertTree_Rec(root.left)
        root.left = leftChild
        root.right = rightChild
        return root
    
    def invertTree_DFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root