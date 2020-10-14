# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 16:47:12 2020

@author: c0096

LeetCode
94. Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:
    1
     \
      2
     /  
    3
    
Input: root = [1,null,2,3]
Output: [1,3,2]
"""
import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = list()
        self.inorder(root,stack)
        return stack
    
    def inorder(self,root,stack):
        if not root : return
        self.inorder(root.left,stack)
        stack.append(root.val)       
        self.inorder(root.right,stack)