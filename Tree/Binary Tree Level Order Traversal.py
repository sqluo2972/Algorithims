# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:56:50 2020

@author: c0096

LeetCode
102. Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

"""
import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans,currentLevel = [],[]
        if not root : return ans
        currentLevel.append(root)
        
        while currentLevel:
            ans.append([node.val for node in currentLevel])
            nextLevel = []
            
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
                    
            currentLevel = nextLevel
            
        return ans
            