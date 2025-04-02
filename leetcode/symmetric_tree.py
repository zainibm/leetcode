'''
Symmetric Tree
https://leetcode.com/problems/symmetric-tree
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root) -> bool:
    if not root:
        return True
    return checkSub(root.left, root.right)

def checkSub(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val) and (checkSub(p.left, q.right)) and (checkSub(p.right, q.left))

node_1 = TreeNode(1)
node_1.left = TreeNode(2)
node_1.left.left = TreeNode(3)
node_1.left.right = TreeNode(4)
node_1.right = TreeNode(2)
node_1.right.left = TreeNode(4)
node_1.right.right = TreeNode(3)
print(isSymmetric(node_1)) # True

node_2 = TreeNode(1)
node_2.left = TreeNode(2)
node_2.left.right = TreeNode(2)
node_2.right = TreeNode(2)
node_2.right.right = TreeNode(2)
print(isSymmetric(node_2)) # False