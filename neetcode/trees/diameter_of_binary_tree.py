'''
Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree
https://neetcode.io/problems/binary-tree-diameter
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root) -> int:
    if not root:
        return 0
    diameter = 0
    left = findHeight(root.left)
    right = findHeight(root.right)
    diameter = left + right
    sub_left = diameterOfBinaryTree(root.left)
    sub_right = diameterOfBinaryTree(root.right)
    sub_root = max(sub_left, sub_right)
    return max(diameter, sub_root)

def findHeight(root):
    if not root:
        return 0
    left = 1 + findHeight(root.left)
    right = 1 + findHeight(root.right)
    return max(left, right)

node = TreeNode(1)
node.left = TreeNode(2)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right = TreeNode(3)
print(diameterOfBinaryTree(node)) # 3

node_2 = TreeNode(1)
node_2.right = TreeNode(2)
node_2.right.left = TreeNode(3)
node_2.right.right = TreeNode(4)
node_2.right.right.right = TreeNode(5)
node_2.right.right.right.right = TreeNode(6)
print(diameterOfBinaryTree(node_2)) # 4