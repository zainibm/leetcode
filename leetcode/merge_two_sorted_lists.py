'''
Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists
https://neetcode.io/problems/merge-two-sorted-linked-lists
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    root = ListNode()
    curr = root
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    if list1 is not None:
        curr.next = list1
    if list2 is not None:
        curr.next = list2
    return root.next

node_a = ListNode(1)
node_b = ListNode(2)
node_c = ListNode(4)
node_a.next = node_b
node_b.next = node_c

node_d = ListNode(1)
node_e = ListNode(3)
node_f= ListNode(4)
node_d.next = node_e
node_e.next = node_f

'''
sorted_ll = mergeTwoLists(node_a, node_d)
while sorted_ll is not None:
    print(sorted_ll.val)
    sorted_ll = sorted_ll.next
'''