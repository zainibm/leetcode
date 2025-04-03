'''
Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    result = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    inorder(root)
    return result

node_1 = TreeNode(1)
node_1.right = TreeNode(2)
node_1.right.left = TreeNode(3)
print(inorderTraversal(node_1)) # [1, 3, 2]

node_2 = TreeNode(1)
node_2.left = TreeNode(2)
node_2.left.left = TreeNode(4)
node_2.left.right = TreeNode(5)
node_2.left.right.left = TreeNode(6)
node_2.left.right.right = TreeNode(7)
node_2.right = TreeNode(3)
node_2.right.right = TreeNode(8)
node_2.right.right.left = TreeNode(9)
print(inorderTraversal(node_2)) # [4, 2, 6, 5, 7, 1, 3, 9, 8]