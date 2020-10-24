# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 23:12:51 2020

LeetCode

96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

 

Constraints:

    1 <= n <= 19


"""

class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2,n+1):
            for j in range(i):
                dp[i] += dp[i-j-1] * dp[j]
                
"""

if n = 0 : Empyt tree still is a binary search tree . dp[0] = 1
if n = 1 : Root is one and its left and right child are empty dp[1] = dp[0]*dp[0] = 1

if n = 2 :   1       1               dp[2]  =  dp[1]*dp[0] + dp[0]*dp[1]
            /         \
           2           2
           
if n = 5 

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3           

dp[2]*dp[0]+dp[1]*dp[1]+dp[0]*dp[2]

dp[n] = dp[n-1]*dp[0]+dp[n-2]*dp[1]+.....+dp[0]*dp[n-1]

"""