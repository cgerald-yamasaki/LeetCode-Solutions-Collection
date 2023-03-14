# 101. Symmetric Tree

# Given the root of a binary tree, check whether it is a mirror of
# itself (i.e., symmetric around its center).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# alternate solution, with some guidance from posted solutions
# works, ~54.96th percentile for runtime, 52.37th for memory
# ... or 92.87th for runtime...
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkTwo(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if node1 == None and node2 == None:
                return True
            if node1 == None or node2 == None:
                return False
            if (node1.left == None and node2.right != None) or (node1.right == None and node2.left != None):
                return False
            if node1.left != None and node2.right != None:
                if node1.left.val != node2.right.val: return False
            if node1.right != None and node2.left != None:
                if node1.right.val != node2.left.val: return False
            if checkTwo(node1.left, node2.right) and checkTwo(node1.right, node2.left):
                return True
            else: return False
        return checkTwo(root, root)

# works, ~35.42nd percentile for runtime, ~14.61st for memory
# ... or 16.41st for runtime and 90.47th for memory...
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if root == None: return True
#         node1 = root
#         node2 = root
#         queue = [root, root]
#         while queue != []:
#             node1 = queue.pop(0)
#             node2 = queue.pop(0)
#             if (node1.left == None and node2.right != None) or (node1.right == None and node2.left != None):
#                 return False
#             if node1.left != None and node2.right != None:
#                 if node1.left.val != node2.right.val: return False
#                 queue.append(node1.left)
#                 queue.append(node2.right)
#             if node1.right != None and node2.left != None:
#                 if node1.right.val != node2.left.val: return False
#                 queue.append(node1.right)
#                 queue.append(node2.left)
#         return True