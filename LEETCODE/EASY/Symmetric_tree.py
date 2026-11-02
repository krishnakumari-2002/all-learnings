# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def IsMirror(left,right):
            if left is None and right is None:
                return True

            if left is None or right is None:
                return False
                
            if left.val!=right.val:
                return False

            return IsMirror(left.left,right.right) and \
                    IsMirror(left.right,right.left)
        return IsMirror(root.left,root.right)
