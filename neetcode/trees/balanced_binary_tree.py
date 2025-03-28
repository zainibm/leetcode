'''
Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree
https://neetcode.io/problems/balanced-binary-tree
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root) -> bool:
    if not root:
        return True
    left = isBalanced(root.left)
    right = isBalanced(root.right)
    if (abs(left-right) > 1):
        return False
    return True
    
def height(root):
    if not root:
        return 0
    left = 1 + height(root.left)
    right = 1 + height(root.right)
    return max(left, right)

node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)
print(isBalanced(node)) # True