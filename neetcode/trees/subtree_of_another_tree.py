'''
Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree
https://neetcode.io/problems/subtree-of-a-binary-tree
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isSubtree(root, subRoot) -> bool:
    if subRoot == None:
        return True
    if root == None:
        return False
    if isSameTree(root, subRoot):
        return True
    return (isSubtree(root.left, subRoot)) or (isSubtree(root.right, subRoot))
    
def isSameTree(root, subRoot):
    if not root and not subRoot:
        return True
    if root and subRoot and root.val == subRoot.val:
        return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)
    else:
        return False

node_1 = TreeNode(3)
node_1.left = TreeNode(4)
node_1.left.left = TreeNode(1)
node_1.left.right = TreeNode(2)
node_1.right = TreeNode(5)
node_2 = TreeNode(4)
node_2.left = TreeNode(1)
node_2.right = TreeNode(2)
print(isSubtree(node_1, node_2)) # True