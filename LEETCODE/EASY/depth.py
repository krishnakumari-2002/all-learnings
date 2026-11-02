class Solution(object):
    def maxDepth(self, root):
        def depth(node):
            if node is None:
                return 0
            left_count=depth(node.left)
            right_count=depth(node.right)
            if right_count>left_count:
                max_count=right_count
            else:
                max_count=left_count
            return max_count+1
        return depth(root)
        
        
           