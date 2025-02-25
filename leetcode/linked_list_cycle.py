'''
Linked List Cycle
https://leetcode.com/problems/linked-list-cycle
Re-solve using fast and slow pointers
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head) -> bool:
    s = set()
    curr = head
    while curr:
        if curr not in s:
            s.add(curr)
            curr = curr.next
        else:
            return True
    return False

fourth = ListNode(-4)
third = ListNode(0)
second = ListNode(2)
first = ListNode(3)
fourth.next = second
third.next = fourth
second.next = third
first.next = second
print(hasCycle(first)) # True

node = ListNode(-1)
print(hasCycle(node)) # False