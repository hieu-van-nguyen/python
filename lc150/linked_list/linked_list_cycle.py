from typing import Optional
from lc150.linked_list.list_node import ListNode

class Solution:
    def hasCycleV1(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr = head
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False
    
    def hasCycleV2(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
