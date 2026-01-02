from typing import Optional
from lc150.graph.graph_node import GraphNode

class Solution:
    # Time complexity: O(V + E)
    # Space complexity: O(V)
    def cloneGraph(self, node: Optional[GraphNode]) -> Optional[GraphNode]:
        map = {}

        def dfs(node):
            if node in map:
                return map[node]
            clone = GraphNode(node.val)
            map[node] = clone
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone
        return dfs(node) if node is not None else None
        