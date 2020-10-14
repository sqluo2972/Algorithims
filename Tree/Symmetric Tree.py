# -*- coding: utf-8 -*-
"""
LeetCode
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
            self.val = val         
            self.left = left
            self.right = right
        
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root :
            return True
        
        stack = [(root.left,root.right)]

        while stack:
            l,r = stack.pop()
            
            if not l and not r :
                continue
            elif not l or not r or (l.val != r.val):
                return False
        
            stack.append((l.left,r.right))
            stack.append((l.right,r.left))
            
        return True