'''
Reorder List
https://leetcode.com/problems/reorder-list
https://neetcode.io/problems/reorder-linked-list
Re-solve using pointers
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    ll = []
    curr = head
    while curr:
        ll.append(curr)
        curr = curr.next
    curr = ll[0]
    check = True
    i = 1
    while i*2 <= len(ll):
        if not check:
            curr.next = ll[i]
            i += 1
        else:
            curr.next = ll[len(ll)-i]
        check = not check
        curr = curr.next
    curr.next = None

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
print(node.val, node.next.val, node.next.next.val, node.next.next.next.val) # [1, 2, 3, 4]
reorderList(node)
print(node.val, node.next.val, node.next.next.val, node.next.next.next.val) # [1, 4, 2, 3]