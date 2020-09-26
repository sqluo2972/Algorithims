# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 17:04:26 2020

LeetCode
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

 

Constraints:

    intervals[i][0] <= intervals[i][1]


"""
import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = list()
        
        for i in sorted(intervals,key = lambda i:i[0]):
            if result and i[0] <= result[-1][1]:
                result[-1][1] = max(i[1],result[-1][1])      #[1,5][2,4] -> [1,5]
            else:
                result.append(i)
                
        return result