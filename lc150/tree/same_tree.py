from collections import deque
from typing import Optional
from lc150.tree.tree_node import TreeNode

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(h)
    def isSameTree(self, p: Optional[TreeNode], q:Optional[TreeNode]) -> bool:
        if not p or not q:
            return p is None and q is None
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    # Time complexity: O(n)
    # Space complexity: O(n)
    def isSameTree_DFS(self, p: Optional[TreeNode], q:Optional[TreeNode]) -> bool:
        if not p or not q:
            return p is None and q is None
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
        return True
    
    # Time complexity: O(n)
    # Space complexity: O(n)
    def isSameTree_BFS(self, p: Optional[TreeNode], q:Optional[TreeNode]) -> bool:
        if not p or not q:
            return p is None and q is None
        
        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            nodeP = q1.popleft()
            nodeQ = q2.popleft()

            if not nodeP and not nodeQ:
                continue
            if not nodeP or not nodeQ or nodeP.val != nodeQ.val:
                return False
            
            q1.append(nodeP.left)
            q1.append(nodeP.right)
            q2.append(nodeQ.left)
            q2.append(nodeQ.right)
        return True