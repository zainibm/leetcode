'''
Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head) -> bool:
    stack = []
    curr = head
    while curr:
        stack.append(curr.val)
        curr = curr.next
    curr = head
    while curr:
        if not curr.val == stack.pop():
            return False
        curr = curr.next
    return True

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(2)
node.next.next.next = ListNode(1)
print(isPalindrome(node)) # True