'''
Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree
https://neetcode.io/problems/invert-a-binary-tree
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if not root:
        return
    temp = root.left
    root.left = root.right
    root.right = temp
    invertTree(root.left)
    invertTree(root.right)
    return root

node = TreeNode(4)
node.left = TreeNode(2)
node.left.left = TreeNode(1)
node.left.right = TreeNode(3)
node.right = TreeNode(7)
node.right.left = TreeNode(6)
node.right.right = TreeNode(9)
print(node.val, node.left.val, node.right.val, node.left.left.val, node.left.right.val, node.right.left.val, node.right.right.val) # [4, 2, 7, 1, 3, 6, 9]
invertTree(node)
print(node.val, node.left.val, node.right.val, node.left.left.val, node.left.right.val, node.right.left.val, node.right.right.val) # [4, 7, 2, 9, 6, 3, 1]