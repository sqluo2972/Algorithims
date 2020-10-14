# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:42:29 2020

LeetCode
105. Construct Binary Tree from Preorder and Inorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7


"""
import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            value = preorder.pop(0)
            index = inorder.index(value)
            root = TreeNode(value)
            root.left = self.buildTree(preorder,inorder[0:index])
            root.right = self.buildTree(preorder,inorder[index+1:])
            return root