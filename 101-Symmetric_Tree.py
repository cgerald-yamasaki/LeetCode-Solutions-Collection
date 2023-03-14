# 101. Symmetric Tree

# Given the root of a binary tree, check whether it is a mirror of
# itself (i.e., symmetric around its center).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# works, ~35.42nd percentile for runtime, 14.61st for memory
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None: return True
        node1 = root
        node2 = root
        queue = [root, root]
        while queue != []:
            node1 = queue.pop(0)
            node2 = queue.pop(0)
            if (node1.left == None and node2.right != None) or (node1.right == None and node2.left != None):
                return False
            if node1.left != None and node2.right != None:
                if node1.left.val != node2.right.val: return False
                queue.append(node1.left)
                queue.append(node2.right)
            if node1.right != None and node2.left != None:
                if node1.right.val != node2.left.val: return False
                queue.append(node1.right)
                queue.append(node2.left)
        return True