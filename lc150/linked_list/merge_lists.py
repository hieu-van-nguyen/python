from typing import Optional
from lc150.linked_list.list_node import ListNode

def mergeTwoListsRec(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    if list1.val <= list2.val:
        list1.next = mergeTwoListsRec(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoListsRec(list1, list2.next)
        return list2
    
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummyHead = node = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
        node = node.next
    node.next = list1 or list2
    return dummyHead.next
