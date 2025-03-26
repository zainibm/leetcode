'''
Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree
https://neetcode.io/problems/depth-of-binary-tree
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root) -> int:
    if not root:
        return 0
    left = 1 + maxDepth(root.left)
    right = 1 + maxDepth(root.right)
    return max(left, right)

node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(17)
print(node.val, node.left.val, node.right.val, node.left.left, node.left.right, node.right.left.val, node.right.right.val) # [3, 9, 20, None, None, 15, 7]
print(maxDepth(node)) # 3