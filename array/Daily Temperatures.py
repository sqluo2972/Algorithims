# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 23:52:05 2020


739. Daily Temperatures

Given a list of daily temperatures T, return a list such that, for each day in the input, 
tells you how many days you would have to wait until a warmer temperature. 
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], 
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. 
Each temperature will be an integer in the range [30, 100]. 
"""
import List

class Solution:      # this solution is on LeetCode
    def dailyTemperatures(self, T: List[int]) -> List[int]:         
            
            n , right_max = len(T),-1
            result = [0] * n
            
            for i in range(n-1,-1,-1):         #from back to front
                if T[i] >= right_max:
                    right_max = T[i]                  
                else:
                    days = 1                
                    while T[i+days] <= T[i]:
                        days += result[i+days]  
                        
                    result[i] = days
                    
            return result
        