from typing import Optional
from lc150.linked_list.list_node import ListNode

def reverseListRec(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    newHead = head
    if head.next:
        newHead = reverseListRec(head.next)
        head.next.next = head
    head.next = None
    return newHead

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev
