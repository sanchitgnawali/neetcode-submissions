# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, low, high):

            if not node:
                return True

            if low >= node.val or high <= node.val:
                return False
            
            left = validate(node.left, low, node.val)
            right = validate(node.right, node.val, high)

            return left & right

        return validate(root, float('-inf'), float('inf'))