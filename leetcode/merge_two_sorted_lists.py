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

node_1 = ListNode(4)
node_1 = ListNode(2)
node_1 = ListNode(1)
node_1.next = node_1
node_1.next = node_1

node_2 = ListNode(4)
node_2 = ListNode(3)
node_2= ListNode(1)
node_2.next = node_2
node_2.next = node_2

'''
sorted_ll = mergeTwoLists(node_1, node_2) => [1, 1, 2, 3, 4, 4]
while sorted_ll is not None:
    print(sorted_ll.val)
    sorted_ll = sorted_ll.next
'''