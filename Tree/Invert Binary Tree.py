# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 18:03:49 2020

@author: c0096

LeetCode
226. Invert Binary Tree

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        
            self.val = val
            self.left = left
            self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:       
        if not root : return 
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left,root.right = root.right, root.left
        return root
        
        