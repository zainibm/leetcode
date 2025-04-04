'''
Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None
    return buildTree(nums, 0, len(nums)-1)

def buildTree(nums, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    root = TreeNode(nums[mid])
    root.left = buildTree(nums, start, mid-1)
    root.right = buildTree(nums, mid+1, end)
    return root

node = sortedArrayToBST([-10, -3, 0, 5, 9])

'''
def printTree(root):
    if not root:
        return
    printTree(root.left)
    print(root.val)
    printTree(root.right)

printTree(node) # -10 => -3 => 0 => 5 => 9
'''