'''
Same Tree
https://leetcode.com/problems/same-tree
https://neetcode.io/problems/same-binary-tree
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q) -> bool:
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False

node_p = TreeNode(1)
node_p.left = TreeNode(2)
node_p.right = TreeNode(3)
node_q = TreeNode(1)
node_q.left = TreeNode(2)
node_q.right = TreeNode(3)
print(isSameTree(node_p, node_q)) # True