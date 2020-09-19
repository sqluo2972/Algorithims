# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 14:19:15 2020

@author: c0096

LeetCode

763. Partition Labels

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

 

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

 

Note:

    S will have length in range [1, 500].
    S will consist of lowercase English letters ('a' to 'z') only.

"""
import List 

class Solution:
    def partitionLabels(self, S: str) -> List[int]:       
        result = list()
        last_index = {}
        
        for index,value in enumerate(S):     #get last character index  
            last_index[value] = index
            
       
        break_point = -1       
        index = -1              #record last character index  
        
        for idx,char in enumerate(S):
            index = max(index,last_index[char])
            if idx == index:
                
                result.append(len(S[:index]) - break_point)
                break_point = index
        
        return result