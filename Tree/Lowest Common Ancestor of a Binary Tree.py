# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 22:54:56 2020

@author: c0096

LeetCode

236. Lowest Common Ancestor of a Binary Tree
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

 

Note:

    All of the nodes' values will be unique.
    p and q are different and both values will exist in the binary tree.


"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:    # if p or q was found then return themself
            return root
        
        left,right = None,None
        
        if root.left != None:
            left = self.lowestCommonAncestor(root.left,p,q)
        if root.right != None:
            right = self.lowestCommonAncestor(root.right,p,q)
            
        
        if left and right:      # if left and right return means
            return root         # their parent is LCA
        else:
            return left or right  # example: p was found in left so left return a node
                                # and right was returned None. This means q is below node p
                                # then node where p was found is LCA 
        