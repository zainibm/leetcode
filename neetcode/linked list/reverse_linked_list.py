'''
Reverse Linked List
https://leetcode.com/problems/reverse-linked-list
https://neetcode.io/problems/reverse-a-linked-list
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    if not head or head.next is None:
        return head
    linked = []
    curr = head
    while curr:
        linked.append(curr)
        curr = curr.next
    new_head = linked[-1]
    curr = new_head
    i = len(linked)-2
    while i >= 0:
        next_node = linked[i]
        curr.next = next_node
        curr = next_node
        i -= 1
    curr.next = None
    return new_head

node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_1.next = node_2
node_2.next = node_3
node_3.next = node_4

'''
reversed_ll = reverseList(node_1)
while reversed_ll is not None:
    print(reversed_ll.val)
    reversed_ll = reversed_ll.next
'''