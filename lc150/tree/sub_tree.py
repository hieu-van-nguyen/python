from collections import deque
from typing import Optional
from lc150.tree.tree_node import TreeNode

class Solution:
    def isSubTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        return self.isSubTree(root.left, subRoot) or self.isSubTree(root.right, subRoot)
    
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return root is None and subRoot is None
        if root.val != subRoot.val:
            return False
        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)